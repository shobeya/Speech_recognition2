import os
import pandas as pd

class UserLibriExplorer:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.audio_files = []
        self.metadata = pd.DataFrame()

    def scan_dataset(self):
        print(f"[INFO] Scanning dataset at: {self.dataset_path}")
        for root, dirs, files in os.walk(self.dataset_path):
            for file in files:
                if file.endswith(".flac"):
                    full_path = os.path.join(root, file)
                    self.audio_files.append(full_path)
        print(f"[INFO] Found {len(self.audio_files)} audio files.")

    def load_metadata(self):
        metadata_path = os.path.join(self.dataset_path, "metadata.tsv")
        if os.path.exists(metadata_path):
            self.metadata = pd.read_csv(metadata_path, sep="\t")
            print(f"[INFO] Loaded metadata with shape: {self.metadata.shape}")
        else:
            print(f"[WARNING] Metadata file not found at: {metadata_path}")

    def explore(self):
        self.scan_dataset()
        self.load_metadata()

        print("\n--- Dataset Summary ---")
        print(f"📁 Dataset path: {self.dataset_path}")
        print(f"🎧 Total audio files: {len(self.audio_files)}")

        if not self.metadata.empty:
            print(f"🧾 Metadata columns: {self.metadata.columns.tolist()}")

            # Dynamically check which column to use
            if "client_id" in self.metadata.columns:
                user_col = "client_id"
            elif "User ID" in self.metadata.columns:
                user_col = "User ID"
            else:
                user_col = None

            if user_col:
                print(f"👥 Unique users in metadata: {self.metadata[user_col].nunique()}")
            else:
                print("⚠️ Could not find user ID column in metadata.")

            print(f"🗂️ Sample metadata:\n{self.metadata.head()}")
        else:
            print("⚠️ No metadata loaded.")


if __name__ == "__main__":
    dataset_path = r"C:\Users\rvmut\Downloads\archive (18)\UserLibri\audio_data"
    explorer = UserLibriExplorer(dataset_path)
    explorer.explore()
