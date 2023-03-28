---
layout: page
title: Research
---

My lab studies evolution and immunity. We're particularly interested in understanding how viruses evolve and how they interact with the human immune system. For example, how do viruses such as HIV and SARS-CoV-2 evolve to escape immunity? And how can the immune system reliably differentiate between healthy cells and ones that are cancerous or infected by intracellular pathogens? 

We seek to answer these kinds of questions by bringing together theory and data analysis. Much of our work involves statistical inference. We're striving to understand how we can best learn about biological processes from data. The methods we develop are often inspired by statistical physics, combined with statistical learning, population genetics, and epidemiology.

<br>

<img class="theme" src="{{ "/assets/img/research/viral_evolution.png" | relative_url }}" width="200" height="200"/>

### Virus evolution

Highly mutable pathogens like HIV, influenza, and SARS-CoV-2 are a major problem for human health because they can evolve resistance to immune responses that would otherwise control infection. This is why influenza and SARS-CoV-2 vaccines need regular updates, and one of the key reasons why massive efforts have yet to produce a successful vaccine against HIV.

We aim to build a quantitative, *predictive* understanding of pathogen dynamics at the level of individual hosts and whole populations.

#### Key papers:

<small><b>Inferring effects of mutations on SARS-CoV-2 transmission from genomic surveillance data</b><br>Lee B, Sohail MS, Finney E, Ahmed SF, Quadeer AA, McKay MR, <b>Barton JP</b><br>medRxiv <a href="https://doi.org/10.1101/2021.12.31.21268591">[journal link]</a> <a href="{{ "/assets/pdf/papers/lee-sc2-transmission.pdf" | relative_url }}">[pdf]</a> <a href="https://github.com/bartonlab/paper-SARS-CoV-2-inference">[code]</a></small>

<small><b>MPL resolves genetic linkage in fitness inference from complex evolutionary histories</b><br>Sohail MS<sup>=</sup>, Louie RH<sup>=</sup>, McKay MR<sup>c</sup>, <b>Barton JP</b><sup>c</sup><br>Nature Biotechnology <a href="https://doi.org/10.1038/s41587-020-0737-3">[journal link]</a> <a href="{{ "/assets/pdf/papers/sohail-mpl.pdf" | relative_url }}">[pdf]</a> <a href="{{ "/assets/pdf/papers/sohail-mpl-si.pdf" | relative_url }}">[si]</a> <a href="https://github.com/bartonlab/paper-MPL-inference">[code]</a></small>

<small><b>Paired quantitative and qualitative assessment of the replication-competent HIV-1 reservoir and comparison with integrated proviral DNA</b><br>Lorenzi JC, Cohen YZ, Cohn LB, Kreider EF, <b>Barton JP</b>, Learn GH, Oliveira T, Lavine CL, Horwitz JA, Settler A<br>Proceedings of the National Academy of Sciences, 2016 <a href="https://doi.org/10.1073/pnas.1617789113">[journal link]</a> <a href="{{ "/assets/pdf/papers/lorenzi-qqvoa.pdf" | relative_url }}">[pdf]</a> <a href="{{ "/assets/pdf/papers/lorenzi-qqvoa-si.pdf" | relative_url }}">[si]</a></small>

<!---
<small><b>Scaling laws describe memories of host-pathogen riposte in the HIV population</b><br><b>Barton JP</b>, Kardar M, Chakraborty AK<br>Proceedings of the National Academy of Sciences, 2015 <a href="https://doi.org/10.1073/pnas.1415386112">[journal link]</a> <a href="{{ site.baseurl }}/assets/pdf/papers/barton-hiv-basins.pdf">[pdf]</a> <a href="{{ site.baseurl }}/assets/pdf/papers/barton-hiv-basins-si.pdf">[si]</a></small>
-->

<!---
<small><b>The fitness landscape of HIV-1 gag: advanced modeling approaches and validation of model predictions by in vitro testing</b><br>Mann JK<sup>=</sup>, <b>Barton JP</b><sup>=</sup>, Ferguson AL<sup>=</sup>, Omarjee S, Walker BD, Chakraborty A, Ndung'u T<br>PLoS Computational Biology, 2014 <a href="https://doi.org/10.1371/journal.pcbi.1003776">[journal link]</a> <a href="{{ site.baseurl }}/assets/pdf/papers/mann-gag-landscape.pdf">[pdf]</a> <a href="{{ site.baseurl }}/assets/pdf/papers/mann-gag-landscape-si.pdf">[si]</a></small>
-->

<br>


<img class="theme" src="{{ site.baseurl }}/assets/img/research/innate_immunity.png" width="200" height="200"/>

### Innate immunity

The innate immune system is our first line of defense against invading pathogens, and it also helps to fight cancer and coordinate adaptive immunity. Some innate immune cells use an extremely diverse array of germline-encoded receptors to discriminate between healthy cells ("self") and those which are foreign or infected ("nonself") as well as the direct detection of microbial products. How do innate immune cells, whose receptors are fixed and immutable, manage to protect us from a broad range of continually-evolving pathogens? More broadly, what fundamental principles underlie this mode of pathogen recognition?

<br>

<img class="theme" src="{{ site.baseurl }}/assets/img/research/statistical_inference.png" width="200" height="200"/>

### Statistical inference

More data is available than ever before to probe genetic evolution. Heroic sequencing efforts during the SARS-CoV-2 pandemic have made tens of millions of viral genomes available for analysis. It is also possible to record evolving populations of viruses within chronically-infected hosts, analyzed in our own work [here](https://doi.org/10.1038/ncomms11660).

Recently-developed techniques have also enabled us to look at cellular heterogeneity in fantastic detail. This heterogeneity clearly plays a key role in some aspects of the immune system, but little is understood quantitatively.

One of our goals is to develop methods to efficiently learn from this kind of data, and to use it to predict new behavior.

#### Key papers:

<small><b>Inferring effects of mutations on SARS-CoV-2 transmission from genomic surveillance data</b><br>Lee B, Sohail MS, Finney E, Ahmed SF, Quadeer AA, McKay MR, <b>Barton JP</b><br>medRxiv <a href="https://doi.org/10.1101/2021.12.31.21268591">[journal link]</a> <a href="{{ site.baseurl }}/assets/pdf/papers/lee-sc2-transmission.pdf">[pdf]</a> <a href="https://github.com/bartonlab/paper-SARS-CoV-2-inference">[code]</a></small>

<small><b>MPL resolves genetic linkage in fitness inference from complex evolutionary histories</b><br>Sohail MS<sup>=</sup>, Louie RH<sup>=</sup>, McKay MR<sup>c</sup>, <b>Barton JP</b><sup>c</sup><br>Nature Biotechnology <a href="https://doi.org/10.1038/s41587-020-0737-3">[journal link]</a> <a href="{{ site.baseurl }}/assets/pdf/papers/sohail-mpl.pdf">[pdf]</a> <a href="{{ site.baseurl }}/assets/pdf/papers/sohail-mpl-si.pdf">[si]</a> <a href="https://github.com/bartonlab/paper-MPL-inference">[code]</a></small>

<small><b>ACE: adaptive cluster expansion for maximum entropy graphical model inference</b><br><b>Barton JP</b><sup>c</sup>, De Leonardis E, Coucke A, Cocco S<sup>c</sup><br>Bioinformatics, 2016 <a href="https://doi.org/10.1093/bioinformatics/btw328">[journal link]</a> <a href="{{ site.baseurl }}/assets/pdf/papers/barton-ace.pdf">[pdf]</a> <a href="{{ site.baseurl }}/assets/pdf/papers/barton-ace-si.pdf">[si]</a> <a href="https://github.com/johnbarton/ACE">[code]</a></small>
