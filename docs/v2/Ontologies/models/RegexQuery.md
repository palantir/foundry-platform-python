# RegexQuery

Returns objects where the specified field matches the regex pattern provided. This applies to the non-analyzed
form of text fields. Supported operators:
  - `.` matches any character.
  - `?` repeats the previous character 0 or 1 times.
  - `+` repeats the previous character 1 or more times.
  - `*` repeats the previous character 0 or more times.
  - `{}` defines the minimum and maximum number of times the preceding character can repeat. `{2}` means the
    previous character must repeat only twice, `{2,}` means the previous character must repeat at least twice,
    and `{2,4}` means the previous character must repeat between 2-4 times.
  - `|` is the OR operator.
  - `()` forms a group within an expression such that the group can be treated as a single character.
  - `[]` matches a single one of the characters contained inside the brackets, meaning [abc] matches `a`, `b` or
    `c`. Unless `-` is the first character or escaped with `\` (in which case it is treated as a normal character),
    `-` can be used inside the bracket to create a range of characters, meaning [a-c] matches `a`, `b`, or `c`.
    If the character sequence inside the brackets begins with `^`, the set of characters is negated, meaning
    [^abc] does not match `a`, `b`, or `c`. Otherwise, `^` is treated as a normal character.
  - `"` creates groups of string literals.
  - `\` is used as an escape character. However, \d and \D match digit and non-digit characters respectively, \s 
  and \S match whitespace and non whitespace characters respectively, and \w and \W match word and non word 
  characters respectively.

Either `field` or `propertyIdentifier` can be supplied, but not both.


## Properties
| Name | Type | Required | Description |
| ------------ | ------------- | ------------- | ------------- |
**field** | Optional[PropertyApiName] | No |  |
**property_identifier** | Optional[PropertyIdentifier] | No |  |
**value** | str | Yes |  |
**type** | Literal["regex"] | Yes | None |


[[Back to Model list]](../../../../README.md#models-v2-link) [[Back to API list]](../../../../README.md#apis-v2-link) [[Back to README]](../../../../README.md)
