import csv 
import tkinter as tk

#initial preference all sent to '0'
preference=['0','0','0','0','0','0','0','0','0']
result_label = None
def toggle_preference(index):
    preference[index] = '1' if preference[index] =='0' else '0'
def get_result():
    output=[]
    candiesFiltered=''

    with open('candy-data.csv',mode='r') as file:
        candies = list(csv.reader(file))

        for candy in candies[1:]:
            match = True
            for i in range(9):
                if candy[i+1] != preference[i]:
                    match = False
                    break
            if match:
                output.append(candy)

        output.sort(reverse=True, key=lambda x: float(x[-1]))

        if not output:
            output = sorted(candies[1:], key=lambda x: float(x[-1]), reverse=True)[:5]
            candiesFiltered = "No candies matched your preferences.\nTop 5 Most Liked Candies:\n"
        else:
            topCandyString=f"Top Candy At Our Stop matching your preferences:\n\t{output[0][0]},Price: $ {round(float(output[0][-2]),2)}\n\n"
            candlesFiltered = topCandyString + "\nFiltered Candles:\n"

        for candy in output:
            candiesFiltered +=f"Candy: {candy[0]}, Price: $ {round(float(candy[-2]),2)}\n"

    return candiesFiltered

def show_results():
    global result_label
    if result_label:
        result_label.destroy()

    result_text = get_result()
    result_label = tk.Label(root, text=result_text, justify='left')
    result_label.pack()

def clear_filters():
    global result_label
    for i in range(9):
        preference[i] = '0'
        checkbuttons[i].deselect()
    if result_label:
        result_label.destroy()
        result_label = None

root = tk.Tk()
root.title("PES Candy Store")
root.geometry("400x600")

titleLabel = tk.Label(root, text="PES Candy Store", font=("Helvetica", 16))
titleLabel.pack()

labels = ["chocolate", "fruity", "caramel", "peanutyalmondy", "nougat", "crispedricewafer", "hard", "bar", "pluribus"]
checkbuttons = []

for i, label in enumerate(labels):
    checkbutton = tk.Checkbutton(root, text=label, command=lambda i=i: toggle_preference(i))
    checkbutton.pack(anchor='w')
    checkbuttons.append(checkbutton)

tk.Button(root, text="Show Results", command=show_results).pack(pady=10)
tk.Button(root, text="Clear Filters", command=clear_filters).pack(pady=10)

root.mainloop()