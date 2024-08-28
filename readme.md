# Simulador de Sinal PWM

Este projeto permite visualizar sinais PWM (Pulse Width Modulation) gerados a partir de uma string de texto. O sinal PWM resultante é exibido em um gráfico interativo.


### Clone o repositório
```bash
git clone https://github.com/JoaoVictorFBarros/Bit_Error_Rate.git
```


### Instalação das Dependências

Se ainda não tiver as bibliotecas instaladas, use:

```
pip install numpy matplotlib tkinter
```

### Executando o Projeto

Para iniciar o simulador, execute:

```
python3 main.py
```
<div align="center">
<img src=print.png width=80%>
</div>

## Conceitos de Transmissão de Dados e PWM

### 1. Modulação por Largura de Pulso (PWM)

PWM é uma técnica usada para transmitir informações e controlar dispositivos variando a largura dos pulsos em um sinal digital. Em um sinal PWM, a largura dos pulsos representa diferentes valores binários:

- **Pulso Largo**: Geralmente representa o valor binário '1'.
- **Pulso Curto**: Geralmente representa o valor binário '0'.

A proporção entre a largura do pulso e o intervalo total de tempo é conhecida como "duty cycle". O PWM é amplamente utilizado em diversas aplicações para transmitir dados e controlar dispositivos.

### 2. Aplicações Práticas do PWM

- **Controle de Motores**: Ajusta a velocidade e o torque dos motores elétricos.
- **Controle de Brilho de LEDs**: Regula a intensidade luminosa dos LEDs.
- **Comunicação Digital**: Transmite dados binários em sistemas digitais, onde a largura dos pulsos pode codificar diferentes bits de informação.

### 3. Funcionamento do Programa

1. **Entrada de Dados**: O usuário insere uma string de texto na interface gráfica. Cada caractere da string é convertido para uma sequência binária de 8 bits.

2. **Geração do Sinal PWM**:
   - **Conversão**: A sequência binária é convertida em um sinal PWM, onde cada bit '1' resulta em um pulso longo e cada bit '0' em um pulso curto.
   - **Configuração dos Pulsos**: A largura dos pulsos é ajustada para representar corretamente os valores binários. Pulsos para '1' têm uma largura de 0.7 segundos, e para '0', 0.3 segundos.

3. **Visualização**:
   - O sinal PWM gerado é exibido em um gráfico, mostrando como o sinal varia ao longo do tempo com base na sequência binária da string fornecida.

Este simulador oferece uma visão prática de como sinais PWM podem ser utilizados para representar dados binários e controlar dispositivos em sistemas eletrônicos e de comunicação.

