import os
from analyzer.text_analyzer import TextAnalyzer

def main():
    analyzer = TextAnalyzer()
    
    input_file = input("Enter the path to your input Excel file: ")
    output_dir = input("Enter the directory where output files should be saved: ")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    text_column = input("\nEnter the column name for topic clustering: ")
    threshold = float(input("Enter similarity threshold (0.0-1.0): "))
    batch_size = int(input("Enter batch size (default 500): ") or 500)
    
    print("\nStarting topic clustering...")
    clustering_results = analyzer.perform_topic_clustering(input_file, text_column, output_dir, threshold, batch_size)
    if clustering_results is not None:
        print(f"Topic clustering complete. Results saved to '{os.path.join(output_dir, 'topic_clustering_results.xlsx')}'")
    else:
        print("Topic clustering failed.")

if __name__ == "__main__":
    main()