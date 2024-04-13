import tkinter as tk
from tkinter import messagebox
import random

def main():
    root = tk.Tk()
    root.title("Генератор  счета матчей Антийой")
    root.geometry("400x300")  # Set window size

    label1 = tk.Label(root, text="Команда 1:")
    label1.grid(row=0, column=0)
    team1_entry = tk.Entry(root)
    team1_entry.grid(row=0, column=1)

    label2 = tk.Label(root, text="Команда 2:")
    label2.grid(row=1, column=0)
    team2_entry = tk.Entry(root)
    team2_entry.grid(row=1, column=1)

    label3 = tk.Label(root, text="Счет команды 1:")
    label3.grid(row=2, column=0)
    team1score_entry = tk.Entry(root)
    team1score_entry.grid(row=2, column=1)

    label4 = tk.Label(root, text="Счет команды 2:")
    label4.grid(row=3, column=0)
    team2score_entry = tk.Entry(root)
    team2score_entry.grid(row=3, column=1)

    generate_button = tk.Button(root, text="Сгенерировать игроков", command=lambda: generate_lineup(root, team1_entry.get(), team2_entry.get(), team1score_entry.get(), team2score_entry.get()))
    generate_button.grid(row=4, column=0, columnspan=2)

    root.mainloop()

def lineSearch(teamName, teamscore):
    file = "Teams.txt"
    with open(file, 'r') as file:
        for line in file:
            if teamName in line:
                team_players = line.split(':')[1].strip().split(', ')
                team_array = [player.strip() for player in team_players]
                return team_array
        return None

def randomize(team_array, teamscore, teamName):
    result = f"Счет для команды {teamName}: {teamscore}\n"
    result += "Забившие игроки:\n"
    for _ in range(int(teamscore)):
        player = random.choice(team_array)
        result += f"{player}\n"
    return result

def generate_lineup(root, team1, team2, team1score, team2score):
    if not team1 or not team2 or not team1score or not team2score:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    team1_array = lineSearch(team1, team1score)
    team2_array = lineSearch(team2, team2score)

    if team1_array is None or team2_array is None:
        messagebox.showerror("Error", "One or both teams not found in file.")
        return

    result = randomize(team1_array, team1score, team1)
    result += randomize(team2_array, team2score, team2)

    result_window = tk.Toplevel(root)
    result_window.title("Сгенерированные игроки")
    result_label = tk.Label(result_window, text=result)
    result_label.pack()

if __name__ == "__main__":
    main()
