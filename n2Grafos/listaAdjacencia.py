
grafo = {
  "RS" : ["SC"],
  "SC" : ["RS", "PR"],
  "PR" : ["SC", "SP"],
  "SP" : ["PR", "RJ", "MG", "MT"],
  "RJ" : ["SP", "ES"],
  "MG" : ["SP", "ES", "DF"],
  "ES" : ["RJ", "MG"],
  "DF" : ["MG"],
  "MT" : ["SP", "PA"],
  "PA" : ["MT", "RR"],
  "RR" : ["PA", "AM"],
  "AM" : ["RR", "TO"],
  "TO" : ["AM", "AP"],
  "AP" : ["TO", "CE"],
  "CE" : ["AP", "PI"],
  "PI" : ["CE", "BA"],
  "BA" : ["PI", "AC"],
  "AC" : ["BA", "RO"],
  "RO" : ["AC", "GO"],
  "GO" : ["RO"]
}