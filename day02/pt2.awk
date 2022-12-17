BEGIN {
  win["A"] = "Y"
  win["B"] = "Z"
  win["C"] = "X"

  draw["A"] = "X"
  draw["B"] = "Y"
  draw["C"] = "Z"

  lose["A"] = "Z"
  lose["B"] = "X"
  lose["C"] = "Y"

  s["X"] = 1
  s["Y"] = 2
  s["Z"] = 3
}

$2 == "X" {
  c += s[lose[$1]]
}

$2 == "Y" {
  c += 3 + s[draw[$1]]
}

$2 == "Z" {
  c += 6 + s[win[$1]]
}

END {
  print c
}
