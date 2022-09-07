
class Solution:
  def numberToWords(self, num: int) -> str:
    if num == 0:
      return "Zero"

    belowTwenty = ["",        "One",       "Two",      "Three",
                   "Four",    "Five",      "Six",      "Seven",
                   "Eight",   "Nine",      "Ten",      "Eleven",
                   "Twelve",  "Thirteen",  "Fourteen", "Fifteen",
                   "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["",      "Ten",   "Twenty",  "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def toWord(num: int) -> str:
      if num < 20:
        s = belowTwenty[num]
      elif num < 100:
        s = tens[num // 10] + " " + belowTwenty[num % 10]
      elif num < 1000:
        s = toWord(num // 100) + " Hundred " + toWord(num % 100)
      elif num < 1000000:
        s = toWord(num // 1000) + " Thousand " + toWord(num % 1000)
      elif num < 1000000000:
        s = toWord(num // 1000000) + " Million " + \
            toWord(num % 1000000)
      else:
        s = toWord(num // 1000000000) + " Billion " + \
            toWord(num % 1000000000)

      return s.strip()

    return toWord(num)
