import html

print('html escape: ', html.escape("This HTML fragment contains a <script>script</script> tag."))

print('\n')
print('html unescape: ', html.unescape("I &hearts; Python's &lt;standard library&gt;."))