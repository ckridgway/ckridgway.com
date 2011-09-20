global_context = {}

def process(path, data):
    import re
    import os

    # Convert Markdown tags
    pattern = re.compile(r'\{%\s+markdown\s+%\}\s+(.+?)\{%\s+endmarkdown\s+%\}', re.S)
    def convertToMarkdown(m):
        import markdown
        return markdown.markdown(m.group(1), extensions = ['meta', 'codehilite'])

    data = pattern.sub(convertToMarkdown, data)

    return global_context, data
