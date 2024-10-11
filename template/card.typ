#set page(
  paper: "a6",
  margin: 1.2cm,
  flipped: true,  

)

#set text(
  font: "Deutschschweizer Basisschrift",
  size: 24pt,
  lang: "de",
)

#let card(body, category: "", code: "", class: "", ladder: "123456", color: "808080", optional: false) = {

  pagebreak(weak: true)
  set text(size: 15pt)
  set align(left + horizon)

  place(
    bottom + left,
    circle(
    radius: 10mm,
    fill: rgb(color))
  )

  place(
    right + top,
    dx: +17mm,
    dy: -17mm,
    rotate(0deg,
    rect(
    width: 10mm,
    height: 100mm,
    fill: gradient.linear(
      if ladder.contains("1") { rgb("#eea320") } else { rgb("#fcf4e4") }, 
      if ladder.contains("2") { rgb("#eea320") } else { rgb("#fcf4e4") }, 
      if ladder.contains("3") { rgb("#97c941") } else { rgb("#f2f9e7") }, 
      if ladder.contains("4") { rgb("#97c941") } else { rgb("#f2f9e7") }, 
      if ladder.contains("5") { rgb("#2c8fce") } else { rgb("#e7f0f9") }, 
      if ladder.contains("6") { rgb("#2c8fce") } else { rgb("#e7f0f9") }, 
      angle: 90deg
    ).sharp(6))
  ))

  
  body

  set text(size: 12pt)
  set align(right + bottom)

  category
  linebreak()
  class + " | " + code
  
  if optional != 0{
  linebreak()
  "Optionales Ziel"
  }
}
