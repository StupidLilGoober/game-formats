# Sprites

| File Format | Extension | Purpose |
| :---: | :---: | :--- |
| Sprite | `.spr` | Store images / animations of game entities. |

A `.spr` sprite consists of a `META.json` file and an ordered collection
of image files.

The `META.json` should contain something similar to this:

```json
{
  "name":"sprite_name",
  "width":32,
  "height":32,
  "fps":8,
  "animations": {
    "idle": [0, 1],
    "walk": [2, 3, 4, 5]
  }
}
```

Each number references the index of a frame. Example:

* `0000.png` -> 1st frame
* `0001.png` -> 2nd frame
* `0002.png` -> 3rd frame

---

> [!TIP]
> All frame filenames should use the same number of digits (zero-padded).
> This ensures they sort correctly in file browsers and when listed 
> programmatically.

> [!TIP]
> To achieve performance similar to a traditional spritesheet, implementations 
> may combine all frames into a single texture after loading. This is optional 
> and is only recommended if it provides a measurable performance benefit.
