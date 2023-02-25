This Python program takes a single integer as input, and expands it to an equivalent arithmetic expression of a size corresponding to the specified depth ("de-solving it"). This is just a silly idea I thought of; I am yet to come up with a reasonable application for it (other than maybe practicing your TI-84 input skills).

Note that the expression tree will not always reach the maximum depth specified due to limitations regarding keeping every operand an integer, as well as avoiding huge numbers that would make the program hang.

### Usage
`python desolver.py <Input integer> <Max depth of expression tree>`

Example output for ``python desolver.py 42 8``:
```
Standard Format:
(((2 + 2) + (((1694400 / ((224296565760 / (6 * 54386)) / ((78044 * 4) / (208 + 228)))) - ((((10 / 2) + (17 * 2)) * 101) / (3 * ((18876 / 132) / (21 - 10))))) / (2 * ((((190 + 365) + (319 - 130)) / ((244992 / 464) / (132 / 6))) - (((35 / 5) - 2) + (2 + (7 + 1))))))) - (((((11 + (2 * (7 - 2))) * (((14 + 1) / 3) - 2)) / ((((550 / 22) - (9 - 4)) / ((13 - 6) - 3)) - 2)) * (((((19 * 11) / 11) * 2) + 2) / ((((16 - 4) - (20 / 4)) + 2) - (((4 * 10) / (3 + 2)) / 2)))) / ((((((399289 - 186631) / (120 + 81)) + ((7611 + 16899) / (126 + 3))) - (((88 * 3) + (4 * 31)) - (2 * (34 + 22)))) / ((5 - 2) * (((9 + 15) / 3) + 1))) / ((((13 - 2) - 2) - (2 + 1)) / 2))))

TeX Format:
(((2 + 2) + \frac{(\frac{1694400}{\frac{\frac{224296565760}{6 \times 54386}}{\frac{78044 \times 4}{(208 + 228)}}} - \frac{(\frac{10}{2} + 17 \times 2) \times 101}{3 \times \frac{\frac{18876}{132}}{(21 - 10)}})}{2 \times (\frac{((190 + 365) + (319 - 130))}{\frac{\frac{244992}{464}}{\frac{132}{6}}} - ((\frac{35}{5} - 2) + (2 + (7 + 1))))}) - \frac{\frac{(11 + 2 \times (7 - 2)) \times (\frac{(14 + 1)}{3} - 2)}{(\frac{(\frac{550}{22} - (9 - 4))}{((13 - 6) - 3)} - 2)} \times \frac{(\frac{19 \times 11}{11} \times 2 + 2)}{((((16 - 4) - \frac{20}{4}) + 2) - \frac{\frac{4 \times 10}{(3 + 2)}}{2})}}{\frac{\frac{((\frac{(399289 - 186631)}{(120 + 81)} + \frac{(7611 + 16899)}{(126 + 3)}) - ((88 \times 3 + 4 \times 31) - 2 \times (34 + 22)))}{(5 - 2) \times (\frac{(9 + 15)}{3} + 1)}}{\frac{(((13 - 2) - 2) - (2 + 1))}{2}}})
```

Corresponding [TeX](https://latexeditor.lagrida.com/):
![](img/tex.png)


### Future Improvements
- [ ] Add more operations/functions
