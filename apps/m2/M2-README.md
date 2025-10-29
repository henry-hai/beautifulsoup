# Milestone 2 - BeautifulSoup Extensions

## Part 2: API Definitions Location

### Milestone 1 APIs Used

#### Task 1: `soup.prettify()`
- **File**: `bs4/element.py`
- **Line**: 2601 (in Tag class)

#### Task 2: Find all hyperlinks (`<a>` tags)
- **File**: `bs4/element.py`
- **Line**: 2715 (in find_all method)

#### Task 3: Print all tags
- **File**: `bs4/element.py`
- **Line**: 2715 (in find_all method)

#### Task 4: Find tags with id attribute
- **File**: `bs4/element.py`
- **Line**: 2715 (in find_all method with attrs parameter)

#### Task 5: `find_parent()`
- **File**: `bs4/element.py`
- **Line**: 992 (in find_parent method)

#### Task 6: Change `<b>` to `<blockquote>`
- **File**: `bs4/element.py`
- **Line**: 552 (in replace_with method)

#### Task 7: Add class attribute to `<p>` tags
- **File**: `bs4/element.py`
- **Line**: 1675 (in Tag.__init__ where attrs is initialized)

### Part 1 APIs Used (SoupStrainer)

#### SoupStrainer class
- **File**: `bs4/filter.py`
- **Line**: 313 (SoupStrainer class definition)

#### SoupStrainer constructor
- **File**: `bs4/filter.py`
- **Line**: 345 (SoupStrainer.__init__ method)

#### BeautifulSoup constructor with parse_only parameter
- **File**: `bs4/__init__.py`
- **Line**: 209 (BeautifulSoup.__init__ method with parse_only parameter)

## Part 3: SoupReplacer Implementation

### Design Decisions

The SoupReplacer API was implemented with the following design:

1. **Constructor**: `SoupReplacer(og_tag, alt_tag)`
   - `og_tag`: Original tag name to replace
   - `alt_tag`: Alternative tag name to replace with

2. **Integration**: Added as optional parameter to BeautifulSoup constructor
   - `BeautifulSoup(html_doc, replacer=soup_replacer)`

3. **Implementation Location**: 
   - **File**: `bs4/__init__.py`
   - **Class**: `SoupReplacer`
   - **Integration**: Modified `BeautifulSoup.__init__()` method

### Key Features

- Tag replacement happens during parsing (not after)
- Memory efficient - no need to traverse tree again
- Similar API design to SoupStrainer for consistency
- Maintains BeautifulSoup's existing functionality

### Usage Example

```python
from bs4 import BeautifulSoup
from bs4 import SoupReplacer

# Create replacer
b_to_blockquote = SoupReplacer("b", "blockquote")

# Use during parsing
soup = BeautifulSoup(html_doc, replacer=b_to_blockquote)
print(soup.prettify())
```
