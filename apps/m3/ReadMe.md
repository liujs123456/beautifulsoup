*Milestone 2: `SoupReplacer(og_tag, alt_tag)`**
  - Extremely great for global renames (like `<b> → <strong>` or something);
  - But it **only renames**—no attribute or structural changes.

*Milestone 3: `SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)`**
  - Runs **during parsing** per tag: can **rename**, **mutate attributes**, and apply richer **side effects**;
  - More flexible for cleaning/normalization tasks.

*Recommendation**
  - Expose a few simple configuration knobs (e.g., rename_map, drop_attrs, add_attrs) 
and translate them internally into M3 transformers; keep the M2 shortcut "b"→"strong" for backward compatibility.

*Why**
 - Cases with zero user code—no callbacks required. For advanced needs, users can still combine M3 callbacks