import os
from PIL import Image
from rich.console import Console
from rich.panel import Panel

console = Console()

def banner():
    ascii_art = """
     ██████╗██╗██╗     ███████╗███╗   ██╗████████╗███████╗
    ██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝╚══███╔╝
    ╚█████╗ ██║██║     █████╗  ██╔██╗ ██║   ██║     ███╔╝ 
     ╚═══██╗██║██║     ██╔══╝  ██║╚██╗██║   ██║    ███╔╝  
    ██████╔╝██║███████╗███████╗██║ ╚████║   ██║   ███████╗
    ╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
                [ METADATA NUKER ]
    """
    console.print(Panel(ascii_art, style="bold blue", expand=False))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    
    path = console.input("[bold yellow]Chemin du dossier ou de l'image : [/bold yellow]")
    
    if os.path.isfile(path):
        files = [path]
    elif os.path.isdir(path):
        files = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    else:
        console.print("[bold red]Chemin invalide.[/bold red]")
        return

    for f_path in files:
        try:
            img = Image.open(f_path)
            data = list(img.getdata())
            img_no_exif = Image.new(img.mode, img.size)
            img_no_exif.putdata(data)
            img_no_exif.save(f_path)
            console.print(f"[green]Nettoyé : {os.path.basename(f_path)}[/green]")
        except Exception as e:
            console.print(f"[red]Erreur sur {f_path} : {e}[/red]")

if __name__ == "__main__":
    main()
