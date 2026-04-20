## About the Project

**Boki** is a virtual assistant powered by a locally hosted large language model, designed to interact with real-world systems through custom integrations.

This project started as an experiment: running a local LLM and accessing it from within a Minecraft server using a Lua program (via ComputerCraft). As my experience with programming, networking, and system design grew, I expanded the original idea into a more flexible and powerful assistant.

The goal of Boki is to explore how far a self-hosted LLM can go as an interactive system: handling requests, calling tools, and integrating with external environments, while remaining fully under the user's control.

This project combines my interests in:

* Large Language Models
* Computer Networks
* Systems Integration

and serves as a playground for experimenting with real-world AI applications.

## Getting Started (WIP)

```bash
./llama.cpp/build/bin/llama-server -m models/gemma-4-E2B-it-Q5_K_M.gguf -ngl 99
./llama.cpp/build/bin/llama-server -ngl 22 -m ~/models/Qwen3-8B-Q4_K_M.gguf
```

> Boki V1 used: Llama-3.2-3B-Instruct-abliterated.Q8_0


| Model       | Number of GPU Layers | Tokens/s |
| :---------: | :------------------: | :------: |
| LLaMA 3.1 8b Q4 | 20-21 | ~16 |
| LLaMA 3.1 8b Q3 | 25 | ~20 |
| Qwen 3 8b Q4 | 21-22 | ~15 |
| Gemma 4 E2B | all | ~73 |

## Features

* **Agentic AI with Tool Access**
  Autonomous assistant capable of querying structured data and executing actions through integrated tools.

* **Database Integration**
  Retrieves and processes relevant information from a connected database to enhance responses and decision-making.

* **Google Calendar Integration**
  Read and create events programmatically, enabling scheduling and time-based task management.

* **Hardware Interaction (Arduino)**
  Interface with a microcontroller to interact with the physical world:

  * Control a display based on "emotion tags"
  * Operate motors and other components

* **Remote Access via VPN**
  Securely access and interact with the assistant from external networks.

## Architecture

Boki is built around a locally hosted large language model served via **llama.cpp** using the `llama-server` API.

The system is composed of the following components:

* **LLM Backend (llama.cpp)**
  Hosts the model locally and exposes an API for inference.

* **Python API Layer**
  Acts as the core orchestrator:

  * Processes user input
  * Sends requests to the LLM
  * Handles responses
  * Manages tool/function calling logic

* **Tooling System**
  Enables the assistant to interact with external systems such as:

  * Database (work in progress)
  * Google Calendar
  * Arduino microcontroller

* **Hardware Layer (Arduino)**
  Receives commands from the backend and performs physical actions, such as:

  * Updating a display based on "emotion tags"
  * Controlling motors and other components

* **Remote Access (VPN)**
  Allows secure external interaction with the assistant.
