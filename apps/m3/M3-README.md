# Milestone 3 - SoupReplacer API Brief

### M2 API: `SoupReplacer(og_tag, alt_tag)`

* **Pros:** Simple, fast, good for one job (renaming tags like `<b>` to `<strong>`).
* **Cons:** Very limited. Can't change attributes or do anything conditional.

### M3 API: `SoupReplacer(name_xformer, attrs_xformer, xformer)`

* **Pros:** Extremely powerful. Lets the user run any Python function on tags during parsing. Can rename tags, add/remove attributes, and perform complex logic.
* **Cons:** More complex for the user. Slightly slower because it runs a function for each tag.

### Recommendation

Implement the **M3 API** for its power and flexibility.

We can keep the M2 constructor as a simple "shortcut" for users, which makes our API backward-compatible and easy for both new and advanced users.