----------------------------------------------------------------------------------
-- File: control_unit.vhd
-- Author: Panagopoulos Nikolaos
-- Year: 2025
--
-- Description: Control Unit implementation for MIPS processor subset.
-- Generates control signals based on Opcode input.
--
-- Copyright (c) Panagopoulos Nikolaos, 2025
-- Με επιφύλαξη παντός δικαιώματος. All rights reserved.
----------------------------------------------------------------------------------


library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.std_logic_signed.all;

entity control_unit is
port( 
    Opcode   : in  std_logic_vector(5 downto 0); 
    RegDst   : out std_logic;
    ALUSrc   : out std_logic;
    MemtoReg : out std_logic;
    RegWrite : out std_logic;
    MemRead  : out std_logic;
    MemWrite : out std_logic;
    Branch   : out std_logic;
    Jump     : out std_logic;
    ALUOp    : out std_logic_vector(1 downto 0); 
    clock, reset : in std_logic
);
end control_unit;

architecture behavior of control_unit is
    signal R_format, Lw, Sw, Beq, Ji : std_logic;
begin
    -- Code to generate control signals using opcode bits
    -- Standard MIPS Opcodes
    R_format <= '1' when Opcode = "000000" else '0';
    Lw       <= '1' when Opcode = "100011" else '0';
    Sw       <= '1' when Opcode = "101011" else '0';
    Beq      <= '1' when Opcode = "000100" else '0';
    Ji       <= '1' when Opcode = "000010" else '0';

    RegDst   <= R_format;
    ALUSrc   <= Lw or Sw;
    MemtoReg <= Lw;
    RegWrite <= R_format or Lw;
    MemRead  <= Lw;
    MemWrite <= Sw;
    Branch   <= Beq;
    Jump     <= Ji;
    
    -- ALUOp: 10 for R-type, 01 for Beq, 00 for Lw/Sw
    ALUOp(1) <= R_format;
    ALUOp(0) <= Beq;

end behavior;
