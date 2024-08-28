import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def string_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

def format_binary_multiline(sequence, line_width=32):
    return '\n'.join(sequence[i:i + line_width] for i in range(0, len(sequence), line_width))

def generate_pwm_signal(bits, pulse_duration=0.5, samples_per_second=100):
    t = np.linspace(0, len(bits) * pulse_duration, int(len(bits) * pulse_duration * samples_per_second))
    pwm_signal = np.zeros_like(t)
    
    for i, bit in enumerate(bits):
        pulse_width = 0.7 if bit == '1' else 0.3
        start = int(i * pulse_duration * samples_per_second)
        end = int((i * pulse_duration + pulse_width) * samples_per_second)
        pwm_signal[start:end] = 1

    return t, pwm_signal

def update_plot(*args):
    entry = entry_string.get()
    
    if not entry:
        ax.clear()
        binary_label['text'] = "Sequência binária: "
        canvas.draw()
        return
    
    binary_sequence = string_to_binary(entry)
    formatted_binary_sequence = format_binary_multiline(binary_sequence)

    binary_label['text'] = f"Sequência binária:\n{formatted_binary_sequence}"

    t, pwm_signal = generate_pwm_signal(binary_sequence)

    ax.clear()
    
    ax.plot(t, pwm_signal, drawstyle='steps-pre')
    ax.set_title(f"PWM Signal for string: '{entry}'")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    
    canvas.draw()

root = tk.Tk()
root.title("PWM Signal Simulator")

main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

instructions_label = tk.Label(main_frame, text="Digite a string para transmitir:")
instructions_label.pack(pady=5)

entry_string = tk.StringVar()
entry_string.trace_add("write", update_plot)

entry_field = tk.Entry(main_frame, textvariable=entry_string, width=30)
entry_field.pack(pady=5)

binary_label = tk.Label(main_frame, text="Sequência binária: ")
binary_label.pack(pady=10)

fig, ax = plt.subplots(figsize=(10, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
