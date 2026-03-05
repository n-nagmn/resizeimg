import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def resize_images():
    files = filedialog.askopenfilenames(
        title="画像を選択（複数可）",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
    )
    
    if not files:
        return

    # 保存先フォルダの選択
    save_dir = filedialog.askdirectory(title="保存先フォルダを選択")
    if not save_dir:
        return

    # リサイズ比率の取得（例: 50%）
    try:
        scale = float(scale_entry.get()) / 100
    except ValueError:
        messagebox.showerror("エラー", "比率は数値で入力してください。")
        return

    success_count = 0
    for file_path in files:
        try:
            with Image.open(file_path) as img:
                new_size = (int(img.width * scale), int(img.height * scale))
                img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
                
                base_name = os.path.basename(file_path)
                save_path = os.path.join(save_dir, f"resized_{base_name}")
                
                # 元の形式で保存
                img_resized.save(save_path)
                success_count += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    messagebox.showinfo("完了", f"{success_count}枚の画像を処理しました。")

# GUI設定
root = tk.Tk()
root.title("画像リサイズツール")
root.geometry("300x200")

label = tk.Label(root, text="リサイズ比率 (%)")
label.pack(pady=10)

scale_entry = tk.Entry(root, justify="center")
scale_entry.insert(0, "50")  # デフォルト50%
scale_entry.pack(pady=5)

btn = tk.Button(root, text="画像を選択して実行", command=resize_images, bg="#4CAF50", fg="white")
btn.pack(pady=20)

root.mainloop()