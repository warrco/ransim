# Ransomware Simulator

## Overview
This project is a **ransomware simulator** designed for **educational and research purposes only**. It helps security professionals and researchers understand how ransomware operates in a controlled environment.

## Disclaimer
**This software is intended for educational and research use only. The author does not condone or support any illegal use of this tool. Deploying ransomware for malicious purposes is illegal and punishable by law. Use this tool only in controlled, legal environments.**

## Features
- Simulates file encryption behavior.
- Demonstrates how ransomware typically interacts with files.
- Can be used to test endpoint security measures.
- Logs actions for analysis and learning purposes.
- Shows an attackers perspective.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/warrco/ransim.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ransim
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
⚠️ **Warning:** Use only in an isolated test environment. Do not run this on sensitive or production systems.

To run the server:
```bash
python server.py
```

To run the client:
```bash
python client.py
```

Note: Anti-Virus solutions will detect and block any attempts to run this software. Solutions must be disabled in the environment where the client will run.

## Legal Notice
By using this software, you agree that:
- You will only use it for lawful and ethical research purposes.
- The author is not responsible for any damage or misuse caused by this tool.

## License
This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.

## Contributing
Contributions are welcome! If you'd like to improve the simulator, feel free to submit a pull request.

## Contact
For inquiries or reporting issues, contact: `your-email@example.com`