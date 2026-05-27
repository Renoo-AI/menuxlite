import re

def main():
    with open('index.html', 'r') as f:
        content = f.read()

    # Find classes in HTML (simple regex)
    # This matches class="some-class" or class='some-class'
    # It also tries to handle template literals briefly
    html_classes = set()
    matches = re.finditer(r'class=["\']([^"\']+)["\']', content)
    for match in matches:
        classes = match.group(1).split()
        for c in classes:
            # Filter out template literal parts
            if not ('${' in c or '?' in c or ':' in c or "'" in c):
                html_classes.add(c)

    # Find classes defined in CSS
    css_classes = set()
    # Find all .classname {
    # This is a bit naive but should work for most well-formatted CSS
    css_matches = re.finditer(r'\.([a-zA-Z0-9_-]+)\s*[{,:]', content)
    for match in css_matches:
        css_classes.add(match.group(1))

    # Find classes used in CSS but not defined (not very useful here)

    blind_classes = html_classes - css_classes
    print("Classes in HTML but not in CSS (Blind Classes):")
    for c in sorted(blind_classes):
        print(f"  - {c}")

    # Also check the other way
    unused_classes = css_classes - html_classes
    # Note: some might be used dynamically in JS
    print("\nClasses in CSS but not directly in HTML (Might be dynamic):")
    for c in sorted(unused_classes):
        print(f"  - {c}")

if __name__ == "__main__":
    main()
