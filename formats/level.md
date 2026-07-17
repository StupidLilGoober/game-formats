# Level

It's just like the other formats in the sense that it's a renamed 
`.zip` archive (`.lvl`).

There are two files:

* `data.json`
* `layout.txt`

## The Data File

The `data.json` file is incredibly simple. It looks something like:

```json
{
  "spawn":[2,2],
  "npcs": [{
    "type": "merchant",
    "x": 2,
    "y": 1
  }]
}
```

As you can see, there is an array of `npcs` and a `spawn`point, which
represents where the player should spawn in.

## The Layout File

`layout.txt` is even simpler. It is a text file representing a 2D grid,
where each comma is a column and each new line is a row. For example,

```csv
1,1,1,1,1,1,1,1,1
1,0,0,0,0,0,0,0,1
1,0,0,0,0,0,0,0,1
1,0,0,0,0,0,0,0,1
1,0,0,0,0,0,0,0,1
1,0,0,0,0,0,0,0,1
1,1,1,1,1,1,1,1,1
```
