# Error Correction Simulator

This project explores how classical error-correcting codes can improve the reliability of digital data transmissions over noisy channels.  
It combines theoretical simulations with a practical implementation involving a Raspberry Pi and a PC communicating over Wi-Fi using raw TCP sockets.

The two coding schemes implemented are:

- **Hamming Code (7,4)** — fast, lightweight, ideal for simple errors  
- **Reed-Solomon Code (255,223)** — robust, used in CDs, QR codes, and space communications

---
## Theoretical Principles

This project is based on the mathematical theory of **error-correcting codes**, which are fundamental tools in digital communication systems. The objective is to **ensure data integrity** when transmitting information over a noisy channel.

### Problem Statement

When digital data is transmitted (via a wireless network, physical storage, etc.), it is exposed to **random noise** that can flip bits or corrupt symbols. The receiver might thus receive a message different from the one that was originally sent.

### Mathematical Model: Binary Symmetric Channel (BSC)

The transmission channel is modeled as a **Binary Symmetric Channel (BSC)**. In this model:

- Each bit has a probability `p` of being flipped during transmission.
- Errors occur **independently** across bits.
- This simulates real-world noise in a mathematically tractable way.

### Redundancy and Error Correction

To detect and correct such errors, **redundancy** is introduced into the message through special encoding schemes. The sender encodes the original message into a longer codeword, allowing the receiver to recover the original message even if some bits were altered.

### Implemented Codes

Two classical error-correcting codes are implemented and compared:

#### 1. Hamming Code (7,4)

- Encodes 4 bits of data into 7 bits.
- Can **detect and correct** any single-bit error.
- Based on linear algebra over **binary fields** (`𝔽₂`), using parity-check and generator matrices.
- Efficient but limited in correcting multiple errors.

#### 2. Reed-Solomon Code (255,223)

- Encodes 223 symbols into 255 symbols over **finite fields** (`𝔽₂⁸`).
- Can correct up to 16 symbol errors.
- Based on **polynomial interpolation** and evaluation over Galois Fields.
- Used in real-world systems like CDs, QR codes, and satellite communication due to its high resilience.

### Code Structure and Decoding

Both codes follow this general workflow:

1. **Encoding**: Apply a deterministic function that maps original data to a codeword.
2. **Transmission**: Simulate errors via the BSC.
3. **Decoding**: Use algebraic algorithms (syndrome decoding, Berlekamp-Massey, etc.) to recover the original message.


---------
## Why this project?

In any real communication system, data can be altered by noise — whether over the air, on disk, or in memory.  
This project was born from a simple question: *How can we ensure that what is received is exactly what was sent?*

By simulating and then testing real transmissions with error correction, the goal was to understand:

- How errors appear and propagate  
- How redundancy and structure help protect data  
- How theory meets practice in embedded systems and communication protocols

---

## What’s inside

- A full Python simulation of a Binary Symmetric Channel (BSC) with adjustable noise  
- Two full encoding/decoding chains: Hamming and Reed-Solomon  
- A real-life transmission test over Wi-Fi, Raspberry Pi to PC (using TCP sockets)  
- Visualization tools to compare performance as noise increases  

---

## Technologies

- Python 3  
- NumPy  
- `reedsolo` (for Reed-Solomon codes)  
- Socket programming (TCP)  
- Matplotlib (for plots)  

---

## Project Structure

| File                                                         | Description                                                      |
|--------------------------------------------------------------|-----------------------------------------------------------------|
| [simulate_bsc_channel.py](./simulate_bsc_channel.py)         | Simulates a noisy binary channel and applies error correction   |
| [sender_no_encoding_pi.py](./sender_no_encoding_pi.py)       | Sends raw data (no encoding) from Raspberry Pi                  |
| [sender_hamming_pi.py](./sender_hamming_pi.py)               | Sends Hamming-encoded messages                                  |
| [sender_reed_solomon_pi.py](./sender_reed_solomon_pi.py)     | Sends Reed-Solomon encoded messages                             |
| [receiver_no_decoding_pc.py](./receiver_no_decoding_pc.py)   | Receives uncorrected messages on the PC                         |
| [receiver_hamming_pc.py](./receiver_hamming_pc.py)           | Receives and decodes messages using Hamming code               |
| [receiver_reed_solomon_pc.py](./receiver_reed_solomon_pc.py) | Receives and decodes messages using Reed-Solomon               |
| [performance_graphs.py](./performance_graphs.py)             | Generates performance graphs based on simulation results        |
| [Optimisation_des_transmissions_numériques.pdf](./Optimisation_des_transmissions_numériques.pdf) | Full technical report (in French), including math, code structure, results ||

---
## How to use it

Install the dependencies:
```bash
pip install numpy reedsolo matplotlib
```

### To run a local simulation:
```bash
python simulate_bsc_channel.py
```

### To test real transmission (Raspberry Pi → PC):

1. Start a `receiver_(.....).py` script on the PC
2. Run the corresponding `sender_(...).py` script on the Pi
3. Make sure to update IP addresses and ports in the code if needed

---

## Example result

As the noise increases, Hamming's correction rate quickly drops, while Reed-Solomon remains effective up to ~40% noise.

> A performance comparison graph is available in the `/assets` folder .

---

## About the author

Mohammed Amine Mazouz  
Preparatory Classes Math & Physics in Morocco  
Interested in cybersecurity, error correction, embedded systems, and applied mathematics.

I'm always open to discuss this project or related topics.  
You can reach me via [LinkedIn](https://www.linkedin.com/in/mohamed-amine-mazouz-9a1b4536b/) or directly through this repository.

---

## License

This project is released under the MIT License.
Feel free to explore, modify, or build upon it.

