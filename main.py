import tkinter as tk
from tkinter import ttk

def calculate_even_placements(length, edge_placement):
    placements = []

    adjusted_length = length if edge_placement else length + 2

    for num_objects in range(2, adjusted_length + 1):
        step_size = (adjusted_length - 1) // (num_objects - 1)

        if (adjusted_length - 1) % (num_objects - 1) == 0:
            positions = [i * step_size + 1 for i in range(num_objects)]

            if not edge_placement:
                positions = positions[1:-1]
                positions = [x - 1 for x in positions]

            placements.append(positions)

    return placements

def display_results():
    try:
        for widget in results_frame.winfo_children():
            widget.destroy()

        length = int(entry_length.get())
        edge_placement = var_edge_placement.get()

        placements = calculate_even_placements(length, edge_placement)

        if placements:
            placements = [nested_list for nested_list in placements if nested_list and len(nested_list) != length]
            for i, placement in enumerate(placements, start=1):
                option_frame = ttk.LabelFrame(results_frame, text=f"Option {i}:")
                option_frame.pack(fill="x", pady=5, padx=5)

                result_text = f"Amount of objects: {len(placement)}\nPositions: {placement}"
                label = tk.Label(option_frame, text=result_text, justify="left", wraplength=350)
                label.pack(anchor="w", padx=10, pady=5)
        else:
            no_options_label = tk.Label(results_frame, text="No even placements possible.")
            no_options_label.pack(anchor="w", padx=10, pady=5)

        results_canvas.configure(scrollregion=results_canvas.bbox("all"))

    except ValueError:
        error_label = tk.Label(results_frame, text="Please enter a valid number.")
        error_label.pack(anchor="w", padx=10, pady=5)
        results_canvas.configure(scrollregion=results_canvas.bbox("all"))

root = tk.Tk()
root.title("Even Object Placement")
root.geometry("400x400")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter the length:").grid(row=0, column=0, padx=5)
entry_length = tk.Entry(input_frame)
entry_length.grid(row=0, column=1, padx=5)

calculate_button = tk.Button(input_frame, text="Calculate Placements", command=display_results)
calculate_button.grid(row=0, column=2, padx=5)

var_edge_placement = tk.BooleanVar()
var_edge_placement.set(True)
edge_placement_check = tk.Checkbutton(root, text="Start and end with an object", variable=var_edge_placement)
edge_placement_check.pack(pady=5)

results_frame = tk.Frame(root)
results_canvas = tk.Canvas(results_frame)
scrollbar_y = ttk.Scrollbar(results_frame, orient="vertical", command=results_canvas.yview)
scrollbar_x = ttk.Scrollbar(results_frame, orient="horizontal", command=results_canvas.xview)
scrollable_frame = ttk.Frame(results_canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: results_canvas.configure(
        scrollregion=results_canvas.bbox("all")
    )
)

results_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
results_canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

results_frame.pack(fill="both", expand=True, pady=5)
results_canvas.pack(side="left", fill="both", expand=True)
scrollbar_y.pack(side="right", fill="y")
scrollbar_x.pack(side="bottom", fill="x")

results_frame = scrollable_frame
root.resizable(width=False, height=False)
root.mainloop()
