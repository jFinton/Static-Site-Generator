def markdown_to_blocks(markdown):
    results = []
    results = markdown.split("\n\n")
    filtered = []
    for block in results:
        block = block.strip()
        if block != "":
            filtered.append(block)
    return filtered