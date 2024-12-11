# RadarSimNb

<img src="https://github.com/radarsimx/radarsimpy/blob/master/assets/radarsimnb.svg" alt="logo" width="200"/>

`RadarSimNb` is a repository containing Jupyter Notebooks that provide detailed, hands-on examples for using `RadarSimPy`. These notebooks serve as a practical guide to help you get started quickly and effectively. Explore the [examples](https://radarsimx.com/category/examples/) to dive in!

```mermaid
%%{init: {
  'theme': 'default',
  'themeVariables': { 
      'fontSize': '18px',
      'mainBkg': '#ffffff',
      'nodeBkg': '#ffffff'
  },
  'flowchart': {
      'nodeSpacing': 50,
      'rankSpacing': 100,
      'padding': 20,
      'width': 90
  }
}}%%
flowchart RL
  A("RadarSimCpp")
  B("RadarSimPy")
  C("RadarSimLib")
  D("RadarSimM")
  E("RadarSimNb")
  
  B --> A
  C --> A
  D --> C
  E --> B

  classDef default fill:#ffffff,stroke:#53a757,color:#53a757,rx:10,ry:10,padding:0
  class A,B,C,D,E default

  click A "https://radarsimx.com/radarsimx/radarsimcpp/" "RadarSimCpp"
  click B "https://radarsimx.com/radarsimx/radarsimpy/" "RadarSimPy"
  click C "https://radarsimx.com/radarsimx/radarsimlib/" "RadarSimLib"
  click D "https://radarsimx.com/radarsimx/radarsimm/" "RadarSimM"
  click E "https://radarsimx.com/radarsimx/radarsimnb/" "RadarSimNb"

  style A text-decoration:none
  style B text-decoration:none
  style C text-decoration:none
  style D text-decoration:none
  style E text-decoration:none
```
