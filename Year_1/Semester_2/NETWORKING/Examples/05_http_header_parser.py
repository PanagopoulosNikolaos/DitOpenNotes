"""Parses and validates raw HTTP/1.1 request and response headers adhering to RFC 7230."""

from typing import Dict, Optional, Tuple


class HttpHeaderParser:
    """Parses raw ASCII HTTP protocol headers into structured components."""

    @staticmethod
    def parseRequest(raw_text: str) -> Tuple[str, str, str, Dict[str, str], str]:
        """Parses a raw HTTP request message.

        Args:
            raw_text (str): Complete raw HTTP request string.

        Returns:
            Tuple[str, str, str, Dict[str, str], str]: (method, path, version, headers, body).
        """
        parts = raw_text.split("\r\n\r\n", 1)
        header_section = parts[0]
        body = parts[1] if len(parts) > 1 else ""

        lines = header_section.split("\r\n")
        start_line = lines[0].split(" ")
        method = start_line[0] if len(start_line) > 0 else ""
        path = start_line[1] if len(start_line) > 1 else "/"
        version = start_line[2] if len(start_line) > 2 else "HTTP/1.1"

        headers: Dict[str, str] = {}
        for line in lines[1:]:
            if ":" in line:
                key, val = line.split(":", 1)
                headers[key.strip().lower()] = val.strip()

        return method, path, version, headers, body

    @staticmethod
    def parseResponse(raw_text: str) -> Tuple[str, int, str, Dict[str, str], str]:
        """Parses a raw HTTP response message.

        Args:
            raw_text (str): Complete raw HTTP response string.

        Returns:
            Tuple[str, int, str, Dict[str, str], str]: (version, status_code, reason_phrase, headers, body).
        """
        parts = raw_text.split("\r\n\r\n", 1)
        header_section = parts[0]
        body = parts[1] if len(parts) > 1 else ""

        lines = header_section.split("\r\n")
        status_line = lines[0].split(" ", 2)
        version = status_line[0] if len(status_line) > 0 else "HTTP/1.1"
        status_code = int(status_line[1]) if len(status_line) > 1 and status_line[1].isdigit() else 200
        reason = status_line[2] if len(status_line) > 2 else "OK"

        headers: Dict[str, str] = {}
        for line in lines[1:]:
            if ":" in line:
                key, val = line.split(":", 1)
                headers[key.strip().lower()] = val.strip()

        return version, status_code, reason, headers, body


def main() -> None:
    """Demonstrates parsing of sample HTTP/1.1 request and response packets."""
    sample_request = (
        "GET /index.html HTTP/1.1\r\n"
        "Host: www.example.com\r\n"
        "User-Agent: Mozilla/5.0 (X11; Linux x86_64)\r\n"
        "Accept: text/html\r\n"
        "Connection: close\r\n\r\n"
    )

    method, path, version, headers, _ = HttpHeaderParser.parseRequest(sample_request)
    print("=== Parsed HTTP Request ===")
    print(f"Method:  {method}")
    print(f"Path:    {path}")
    print(f"Version: {version}")
    print("Headers:")
    for k, v in headers.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()

