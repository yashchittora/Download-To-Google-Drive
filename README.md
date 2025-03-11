# 🚀 Google Drive Downloader (Colab)

A simple **Google Colab script** that downloads files from a URL and saves them **directly to Google Drive** with a **progress bar**.

## 👥 Features  
✅ **Directly downloads files** from any URL into Google Drive  
✅ **Shows real-time download progress** using `tqdm`  
✅ **Error handling** for invalid URLs or connection failures  
✅ **Fast & optimized for Colab’s high-speed internet**  

---

## 🔧 Installation & Setup  
### **1️⃣ Open Google Colab**  
Click the link below to open the notebook directly in Google Colab:  

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zY4ioMQexUPLIeMchFvZK_ya-3d4k2NH?usp=sharing)  

---

## 🚀 Usage Guide  
### **1️⃣ Run the Script**  
Execute the script by clicking **Run** in Google Colab.  

### **2️⃣ Enter the File URL & Name**  
The script will prompt you to enter:  
🔗 **File URL** – The direct link to the file you want to download  
📂 **Filename** – The desired name for the file (with extension)  

**Example Input:**  
```
🔗 Enter the direct URL of the file to download: https://example.com/file.zip  
📂 Enter the desired filename (including extension): myfile.zip  
```

### **3️⃣ Download Progress Will Appear**  
A **progress bar** will show the real-time download status:  
```
📝 Download Progress:  50%|█████████████         | 2.5M/5M [00:03<00:03, 850KB/s]  
```

### **4️⃣ File Saved in Google Drive**  
After the download completes, your file will be saved inside:  
```
/content/drive/My Drive/myfile.zip  
```
✅ Done! You can now access it from your **Google Drive**.  

---

## 🛠 Troubleshooting  
### **🔹 1. "Mounting Google Drive failed"**  
✅ Solution: Re-run the script and allow permissions for Google Drive.  

### **🔹 2. "Download failed: Check the URL"**  
✅ Solution: Ensure the **URL is correct and publicly accessible**.  

### **🔹 3. "Slow download speed"**  
✅ Solution: Try using a different **mirror URL** (Colab has fast internet).  

---

## 💜 License  
This project is open-source under the **MIT License**. Feel free to contribute!  

---

## 🌟 Contribute  
💡 Found a bug or have an idea? **Submit an issue** or **open a pull request**!  

📩 Reach me at yashchittora.code@gmail.com  

