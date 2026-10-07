\# OPA Tapeout Sprint — Requirements



\## Deadline



\- Design freeze target: October 15, 2026

\- Submission target: October 16, 2026

\- October 17 is contingency only



\## Fabrication Process



\- Platform: SOI

\- Silicon thickness: 220 nm

\- Etch: single full silicon etch

\- Cladding: oxide

\- Fabricated silicon layer: Si 1/0

\- PDK: SiEPIC-EBeam-PDK

\- Layout / verification backend: KLayout + SiEPIC

\- No heater or metal layers for active phase control



\## OPA Architecture



Passive 1x4 optical phased array:



input -> 1x4 splitter -> geometric path delays -> 4 emitters



Relative phase is generated using controlled waveguide path-length differences.



\## Mandatory Devices



\- ANT sweep: 3–5 single-antenna variants

\- OPA4\_EQ: 1x4 equal-phase reference

\- OPA4\_PHI+: 1x4 positive static phase-gradient variant

\- OPA4\_PHI-: 1x4 opposite/alternative phase-gradient variant

\- SPLIT4\_REF: standalone 1x4 distribution reference

\- MZI\_DLY: path-delay calibration structure



\## Stretch Goals



\- 1x8 OPA

\- extra waveguide/bend-loss structures

\- advanced antenna optimization

\- GUI polish



Stretch work must not threaten fabrication submission.



\## Verification Requirements



\- Manufacturing DRC must pass

\- Functional verification must pass

\- Black-box (\_BB) cells must not be modified

\- Final layout must pass openEBL GitHub Actions

\- Submission must be included in a pull request



\## Design Priorities



1\. Verified fabrication artifact

2\. Coherent test structures

3\. Accurate analytical / EM models

4\. GUI

5\. Stretch devices



\## Initial Risks



| Risk | Response |

|---|---|

| Antenna optimization takes too long | Use conservative full-etch antenna and stop novelty work |

| 1x8 routing becomes difficult | Drop 1x8; keep 1x4 baseline |

| Static phase-delay routing causes failures | Simplify phase-gradient variant |

| Custom PCell verification fails | Simplify ports / DevRec / PinRec semantics |

| 3D FDTD takes too long | Use 2D sweep plus analytical model |

| GUI slips schedule | Postpone GUI until after fabrication work is safe |

