# Target #169: Abstract Plate

[Link to the target](https://cssbattle.dev/play/169)

![img](src/images/169_abstract-plate.png)

<br>

```html
<p></p>
<p tol></p>
<p tir></p>
<p tor></p>
<p rhombus></p>
<style>
  body {
    --x: radial-gradient(1q,
      #4FA07B 0 55px,
      #0D1335 55px 65px,
      #4FA07B 65px 85px,
      #0D1335 85px 95px,
      #4FA07B 95px 115px,
      #0D1335 115px 125px,
      #4FA07B 0
    ) #4FA07B;
    background: var(--x) no-repeat;
  }
  p {
    margin: 24 37;
    position: fixed;
    width: 189;
    height: 236;
    background: #FBFAE2;
    clip-path: polygon(100% 50%, 0 0, 0 100%);
  }
  [tor], [tir] {
    margin: 24 158;
    scale: -1;
  }
  [tol], [tor] {
    background: linear-gradient(90deg, #0000 140px, #FBFAE2 0), var(--x) -5px/300px no-repeat;
    width: 160;
    height: 200;
    margin: 42 47;
  }
  [tor] {
    margin: 42 177
  }
  [rhombus] {
    margin: 0;
    width: 65;
    height: 92;
    margin: 97 160;
    clip-path: polygon(50% 26%, 101% 49%, 55% 70%, 0% 49%);
  }
</style>
```

## Attempts
| Attempt | Score | Link |
|:-:|:-:|:-:|
| 1 | 596.42 {891}, 99.9% match | [Link to the solution](src/html/169_abstract-plate_attempt_01.html) |
| 2 | 602.31 {541}, 100.0% match | [Link to the solution](src/html/169_abstract-plate_attempt_02.html) |
| 3 | 612.70 {362}, 100.0% match | [Link to the solution](src/html/169_abstract-plate_attempt_03.html) |
