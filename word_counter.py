import re


def count_words():
    text = input("Enter the text: ").strip()

    if not text:
        print("No text provided.")
        return

    # 转为小写并提取英文单词，忽略标点
    words = re.findall(r"[a-z]+", text.lower())

    if not words:
        print("No words found in the text.")
        return

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\n单词出现次数")
    for word, count in sorted_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    try:
        count_words()
    except (KeyboardInterrupt, EOFError):
        print("\n程序已终止。")
