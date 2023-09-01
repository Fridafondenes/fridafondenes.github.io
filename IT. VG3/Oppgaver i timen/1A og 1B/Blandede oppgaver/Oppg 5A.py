# Oppgave 5: «Påskeformelen» 
# Første påskedag faller ikke på en fast dato. En vanlig definisjon av når første påskedag inntreffer, er første søndag etter første fullmåne på eller etter vårjevndøgn.

# Det finnes formler for å finne datoen i et gitt år. Her skal vi presentere én slik formel. 

# Hold tunga rett i munnen når du leser denne forklaringen, og lag et program som utfører beregningene. Sjekk at programmet gir riktig dato for de siste fem årene.

# Del årstallet med 19, forkast resultatet, men behold resten, a.
# Del årstallet med 100, behold resultatet, b, og resten, c.
# Del b med 4 og behold resultatet, d, og resten, e.
# Del (b + 8) med 25 og behold resultatet, f.
# Del (b – f + 1) med 3 og behold resultatet, g.
# Del (19 ⋅ a + b – d – g + 15) med 30, forkast resultatet og behold resten, h.
# Del c med 4, behold resultatet, i, og resten, k.
# Del (32 + 2 ⋅ e + 2 ⋅ i – h – k) med 7, forkast resultatet, men behold resten, l.
# Del (a + 11 ⋅ h + 22 ⋅ l) med 451 og behold resultatet, m.
# Del (h + l – 7 ⋅ m + 114) med 31, behold resultatet, n, og resten, p.
# Påskedagen faller på dag p + 1 i måned nummer n.

årstall = int(input(("Hva er årstallet i åt? ")))
a = årstall /19
