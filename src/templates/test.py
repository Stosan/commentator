code = '''```go
// This function takes a CodeCommentData object and an echo.Context object and
// generates a list of comments for the code.
func (cm *CodeCommentData) MakeCodeComments(c echo.Context) error {

  // First, we get the code from the echo.Context object.
  code := c.Get("code")

  // Next, we parse the code and generate a list of comments. The comments are
  // generated based on the structure of the code.
  comments := []string{}
  for _, token := range strings.Split(code, " ") {
    if strings.HasPrefix(token, "//") {
      comments = append(comments, token)
    }
  }

  // Finally, we return the list of comments.
  return comments
}'''

# Find the index of the first occurrence of "```go"
first_occurrence = code.find("```go")

# Find the index of the next newline character after the first occurrence
next_newline = code.find("\n", first_occurrence)

# Remove the first line containing "```go"
code = code[next_newline + 1:]

print(code)
