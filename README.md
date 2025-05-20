
# OpenVoice Service - Multi-Voice Ready

## Como usar:

1. Suba seu repositório no GitHub com essa estrutura.
2. Faça deploy no Render usando Docker.
3. Envie requests para /generate-audio passando text, client_id e voice_id.
4. Receba o áudio gerado (.mp3) para cada cliente.

## Exemplo de request:
curl -X POST https://openvoice-seuprojeto.onrender.com/generate-audio -H "Content-Type: application/json" -d '{"text": "Teste de áudio", "client_id": "123", "voice_id": "joao_015"}' --output audio_123.mp3
