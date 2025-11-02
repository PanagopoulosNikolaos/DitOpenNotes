"""
Database manager for VHDL Simulation Platform
Uses TinyDB to store user preferences, simulation history, and code examples
"""

import os
import json
from datetime import datetime
from tinydb import TinyDB, Query
import time

class DatabaseManager:
    def __init__(self, db_path="db.json"):
        """Initialize the database manager."""
        self.db_path = db_path
        self.db = TinyDB(db_path)
        
        # Define tables
        self.preferences = self.db.table('preferences')
        self.code_history = self.db.table('code_history')
        self.simulation_results = self.db.table('simulation_results')
        self.error_logs = self.db.table('error_logs')
        
        # Initialize with default preferences if empty
        if not self.preferences.all():
            self.preferences.insert({
                'dark_mode': False,
                'auto_save': True,
                'clock_frequency': 100,
                'simulation_time': 100,
                'last_updated': datetime.now().isoformat(),
            })
            
        # Add default examples if code history is empty
        if not self.code_history.all():
            self._add_default_examples()
            
    def _add_default_examples(self):
        """Add default code examples to the code history."""
        # JK Flip-Flop Example
        with open("default_codes/jk_flipflop.vhd", "r") as f:
            jk_code = f.read()
            
        self.add_code(
            "JK Flip-Flop",
            jk_code,
            "Example",
            "A JK flip-flop is a bistable multivibrator with two inputs J and K that control the state changes."
        )
        
        # D Flip-Flop Example
        with open("default_codes/d_flipflop.vhd", "r") as f:
            d_code = f.read()
            
        self.add_code(
            "D Flip-Flop",
            d_code,
            "Example",
            "A D flip-flop is a digital electronic circuit used to store one bit of data."
        )
        
        # SR Latch Example
        with open("default_codes/sr_latch.vhd", "r") as f:
            sr_code = f.read()
            
        self.add_code(
            "SR Latch",
            sr_code,
            "Example",
            "An SR latch (Set-Reset latch) is a bistable multivibrator with two inputs, S and R."
        )
        
    def save_preferences(self, preferences):
        """Save user preferences to the database."""
        preferences['last_updated'] = datetime.now().isoformat()
        self.preferences.truncate()
        self.preferences.insert(preferences)
        return True
        
    def get_preferences(self):
        """Get user preferences from the database."""
        prefs = self.preferences.all()
        if prefs:
            return prefs[0]
        else:
            # Default preferences if table is empty
            return {
                'dark_mode': False,
                'auto_save': True,
                'clock_frequency': 100,
                'simulation_time': 100,
            }
            
    def add_code(self, name, code_content, code_type="User", description=""):
        """
        Add code to the history.
        
        Args:
            name (str): Name of the code
            code_content (str): VHDL code content
            code_type (str): Type of code (User, Example, etc.)
            description (str): Description of the code
        
        Returns:
            int: ID of the inserted code
        """
        code_entry = {
            'name': name,
            'code': code_content,
            'type': code_type,
            'description': description,
            'timestamp': datetime.now().isoformat(),
            'times_used': 0
        }
        
        inserted_id = self.code_history.insert(code_entry)
        return inserted_id
        
    def update_code(self, code_id, name=None, code_content=None, description=None):
        """
        Update existing code in the history.
        
        Args:
            code_id (int): ID of the code to update
            name (str, optional): New name
            code_content (str, optional): New code content
            description (str, optional): New description
        
        Returns:
            bool: True if updated, False otherwise
        """
        Code = Query()
        update_dict = {'timestamp': datetime.now().isoformat()}
        
        if name is not None:
            update_dict['name'] = name
            
        if code_content is not None:
            update_dict['code'] = code_content
            
        if description is not None:
            update_dict['description'] = description
            
        # For TinyDB: use a query to update by doc_id
        Code = Query()
        self.code_history.update(update_dict, doc_ids=[code_id])
        return True
        
    def increment_code_usage(self, code_id):
        """
        Increment the usage count for a code.
        
        Args:
            code_id (int): ID of the code
        """
        code = self.code_history.get(doc_id=code_id)
        if code:
            times_used = code.get('times_used', 0) + 1
            self.code_history.update({'times_used': times_used}, doc_ids=[code_id])
            return True
        return False
        
    def get_code_history(self, code_type=None, limit=10, sort_by='timestamp', sort_order='desc'):
        """
        Get code history, optionally filtered by type.
        
        Args:
            code_type (str, optional): Filter by code type
            limit (int): Maximum number of entries to return
            sort_by (str): Field to sort by
            sort_order (str): Sort order ('asc' or 'desc')
        
        Returns:
            list: Code history entries
        """
        if code_type:
            Code = Query()
            results = self.code_history.search(Code.type == code_type)
        else:
            results = self.code_history.all()
            
        # Sort the results
        if sort_by == 'timestamp':
            results.sort(key=lambda x: x.get('timestamp', ''), reverse=(sort_order == 'desc'))
        elif sort_by == 'name':
            results.sort(key=lambda x: x.get('name', ''), reverse=(sort_order == 'desc'))
        elif sort_by == 'times_used':
            results.sort(key=lambda x: x.get('times_used', 0), reverse=(sort_order == 'desc'))
            
        # Limit the results
        return results[:limit] if limit else results
        
    def get_code_by_id(self, code_id):
        """
        Get code by ID.
        
        Args:
            code_id (int): ID of the code
        
        Returns:
            dict: Code entry or None if not found
        """
        return self.code_history.get(doc_id=code_id)
        
    def log_error(self, error_message, error_type, code_content, simulation_params=None):
        """
        Log an error that occurred during simulation.
        
        Args:
            error_message (str): Error message
            error_type (str): Type of error
            code_content (str): Code that caused the error
            simulation_params (dict, optional): Simulation parameters
        
        Returns:
            int: ID of the inserted error log
        """
        error_entry = {
            'error_message': error_message,
            'error_type': error_type,
            'code': code_content,
            'timestamp': datetime.now().isoformat(),
        }
        
        if simulation_params:
            error_entry['simulation_params'] = simulation_params
            
        inserted_id = self.error_logs.insert(error_entry)
        return inserted_id
        
    def save_simulation_result(self, code_id, code_content, simulation_data, simulation_params):
        """
        Save simulation results.
        
        Args:
            code_id (int): ID of the code that was simulated
            code_content (str): VHDL code content
            simulation_data (dict): Simulation results data
            simulation_params (dict): Simulation parameters
        
        Returns:
            int: ID of the inserted simulation result
        """
        # Convert simulation data to a serializable format
        serializable_data = {}
        for key, value in simulation_data.items():
            if isinstance(value, list):
                serializable_data[key] = value
        
        result_entry = {
            'code_id': code_id,
            'code': code_content,
            'simulation_data': serializable_data,
            'simulation_params': simulation_params,
            'timestamp': datetime.now().isoformat()
        }
        
        inserted_id = self.simulation_results.insert(result_entry)
        
        # Increment the usage count for the code
        self.increment_code_usage(code_id)
        
        return inserted_id
        
    def get_simulation_history(self, code_id=None, limit=10):
        """
        Get simulation history, optionally filtered by code ID.
        
        Args:
            code_id (int, optional): Filter by code ID
            limit (int): Maximum number of entries to return
        
        Returns:
            list: Simulation history entries
        """
        if code_id:
            Simulation = Query()
            results = self.simulation_results.search(Simulation.code_id == code_id)
        else:
            results = self.simulation_results.all()
            
        # Sort by timestamp (newest first)
        results.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        
        # Limit the results
        return results[:limit] if limit else results
        
    def clear_history(self, table_name=None):
        """
        Clear history from a specific table or all tables.

        Args:
            table_name (str, optional): Name of the table to clear ('code_history', 'simulation_results', 'error_logs').
                                      If None, clear all three history tables.
                                      'preferences' table is never cleared by this method.

        Returns:
            bool: True if operation was successful, False otherwise.
        """
        tables_to_clear = []
        re_add_defaults = False

        if table_name:
            if table_name == 'code_history':
                tables_to_clear.append(self.code_history)
                re_add_defaults = True
            elif table_name == 'simulation_results':
                tables_to_clear.append(self.simulation_results)
            elif table_name == 'error_logs':
                tables_to_clear.append(self.error_logs)
            elif table_name == 'preferences':
                 print(f"Warning: Cannot clear 'preferences' table using clear_history.")
                 return False # Explicitly prevent clearing preferences here
            else:
                 print(f"Warning: Table '{table_name}' not found or cannot be cleared.")
                 return False # Indicate invalid input
        else:
            # Clear all default history tables
            tables_to_clear.extend([
                self.code_history,
                self.simulation_results,
                self.error_logs
            ])
            # Check if code_history is actually being cleared before setting flag
            if self.code_history in tables_to_clear:
                re_add_defaults = True

        # Perform truncation
        try:
            # Truncate tables in TinyDB
            for table in tables_to_clear:
                table.truncate()
            # Also clear JSON file entries for these tables
            try:
                with open(self.db_path, 'r+') as f:
                    data = json.load(f)
                    for table in tables_to_clear:
                        data[table.name] = []
                    f.seek(0)
                    f.truncate()
                    json.dump(data, f, indent=4)
            except Exception:
                pass
            # Re-add default examples if code_history was cleared
            if re_add_defaults and hasattr(self, '_add_default_examples') and callable(self._add_default_examples):
                self._add_default_examples()
            return True
        except Exception as e:
            print(f"Error during history clearing: {e}")
            return False
        
    def search_code(self, query, search_in_code=True, search_in_name=True, search_in_description=True):
        """
        Search for code containing the query string.
        
        Args:
            query (str): Search query
            search_in_code (bool): Search in code content
            search_in_name (bool): Search in code name
            search_in_description (bool): Search in code description
        
        Returns:
            list: Matching code entries
        """
        Code = Query()
        results = []
        
        if search_in_code:
            code_results = self.code_history.search(Code.code.search(query, flags=2))  # Case-insensitive
            results.extend(code_results)
            
        if search_in_name:
            name_results = self.code_history.search(Code.name.search(query, flags=2))  # Case-insensitive
            results.extend(name_results)
            
        if search_in_description:
            desc_results = self.code_history.search(Code.description.search(query, flags=2))  # Case-insensitive
            results.extend(desc_results)
            
        # Remove duplicates
        unique_results = []
        seen_ids = set()
        for result in results:
            if result.doc_id not in seen_ids:
                unique_results.append(result)
                seen_ids.add(result.doc_id)
                
        return unique_results