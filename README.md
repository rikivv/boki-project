# projeto-network
Separa coisa dps escreve qlqr coisa direito aki

Boki tinha usado: Llama-3.2-3B-Instruct-abliterated.Q8_0
Usar um modelo 8B Q4. 8B Q4 > 3B Q8


```bash
./llama.cpp/build/bin/llama-server -ngl 21 -m ~/models/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
```
ou

```bash
./llama.cpp/build/bin/llama-server -ngl 25 -m ~/models/Meta-Llama-3.1-8B-Instruct-Q3_K_M.gguf
```
ou
```bash
./llama.cpp/build/bin/llama-server -ngl 22 -m ~/models/Qwen3-8B-Q4_K_M.gguf
```

| Model       | Number of GPU Layers | Tokens/s |
| :---------: | :------------------: | :------: |
| LLaMA 3.1 8b Q4 | 20-21 | ~16 |
| LLaMA 3.1 8b Q3 | 25 | ~20 |
| Qwen 3 8b Q4 | 21-22 | ~15 |