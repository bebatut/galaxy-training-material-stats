- **ATAC-Seq data analysis**
  - Pro:
    - Detailed explanation with pictures and diagrams (*2019-12-06 00:00:00*)
    - a good resource for a training session (*2019-12-12 00:00:00*)
    - The easiness and the clarity of the examples provided.  (*2020-02-25 00:00:00*)
    - so great!!! its so helpful!!!!! (*2020-02-26 00:00:00*)
    - I have to say the full workflow is very useful for the people who did't know this for a long time, thank you so much. but the tool 'Genrich',I  did't find it on the Galaxy... (*2020-03-10 00:00:00*)
    - The degree of detail. I loved that even the parameters for the different tools were explained. I don't know if this is comparable to a real experiment analysis, but it surely felt as that. Congrats! (*2020-03-24 00:00:00*)
    - Entire organization, rationale for the steps taken (*2020-04-12 00:00:00*)
    - Quite easy to follow (*2020-05-28 00:00:00*)
    - Detailed explanation of each step (*2020-05-29 00:00:00*)
    - Thanks (*2020-06-12 00:00:00*)
  - Con:
    - too many steps where you have to 'prepare' data, e.g. sorting the provided bed file (*2019-12-12 00:00:00*)
    - A print version of the tutorial or pdf to save for offline use.  (*2020-02-25 00:00:00*)
    - nothing. (*2020-02-26 00:00:00*)
    - I can't find some tools in Galaxy, (*2020-03-10 00:00:00*)
    - The Genrich tool is only available at the GalaxyEurope server. It would be nice that a warning would be given at the beginning of the tutorial, so that the whole analysis could be done there and avoid migrating data between Galaxy servers. (*2020-03-24 00:00:00*)
    - link to smaple out put or all steps like EMBOSS tutorial does (*2020-04-12 00:00:00*)
    - Bit more interpretation of output (*2020-05-28 00:00:00*)
    - Comparison of two ATAC-Seq datasets (*2020-05-29 00:00:00*)
    - I want to normaized and compared two files(WT VS KO)? What should I do? (*2020-06-12 00:00:00*)

- **DNA Methylation data analysis**
  - Pro:
    - explained quite well (*2019-02-28 00:00:00*)
    - The good explanations during hands-on training (*2019-09-26 00:00:00*)
    - The tutorial is self explanatory and very easy to follow for individual hands on  (*2020-02-04 00:00:00*)
    - The degree of detail. I loved that even the parameters for the different tools were explained. I don't know if this is comparable to a real experiment analysis, but it surely felt as that. Congrats! (*2020-03-24 00:00:00*)
  - Con:
    - velocity (*2019-02-28 00:00:00*)
    - When the tutorial use the softwares in the galaxy plataform (*2019-07-26 00:00:00*)
    - Maybe too different analysis for one day (HiC and epigentics), maybe a longer session for each would help understanding (*2019-09-26 00:00:00*)
    - The Genrich tool is only available at the GalaxyEurope server. It would be nice that a warning would be given at the beginning of the tutorial, so that the whole analysis could be done there and avoid migrating data between Galaxy servers. (*2020-03-24 00:00:00*)

- **EWAS data analysis of 450k data**

  - Con:
    - layout of some tables (*2019-09-11 00:00:00*)

- **Formation of the Super-Structures on the Inactive X**
  - Pro:
    - Clearly explained (*2019-02-11 00:00:00*)
    - the work is well organized, I liked the most questions and answers, also that you also post the output, so we can know that we are going the right direction! (*2019-04-28 00:00:00*)
  - Con:
    - Confusing - somewhere I got lost, I could do what I was asked for, but don't knwo why I did it (*2018-09-18 00:00:00*)
    - Optional Tools and their advantages :) (*2019-02-11 00:00:00*)
    - For example what about single-end data? it will be great to give another example for single-end BAM files? (*2019-04-28 00:00:00*)
    - You put a wrong figure here: Figure 9: Per base sequence quality. It is the same with Figure 3: Per base sequence quality. (*2019-09-27 00:00:00*)
    - You put a wrong figure here: Figure 9: Per base sequence quality. It is the same with Figure 3: Per base sequence quality. (*2019-09-27 00:00:00*)
    - In step 6 it is explained to insert each of the datasets one after the other (with Concatenate datasets tail-to-head). However, one can insert more than one dataset at once with this tool, so why not do that? Also, it should read "Redo for the remaining four outputs of MACS2 callpeak" - it is six in total and in the first step you concatenate two and then add the remaining.  Why are the bedgraph files created if they are not used for anything? (*2020-01-10 00:00:00*)

- **Hi-C analysis of Drosophila melanogaster cells using HiCExplorer**
  - Pro:
    - perfect step by step !!!! (*2018-09-18 00:00:00*)
    - Nothing bad, just I do not have sufficient background knowledge to comprehend everything. Nevertheless, very well-structured for a beginner to learn. (*2019-02-28 00:00:00*)
  - Con:
    - maybe use human data ?? (*2018-09-18 00:00:00*)
    - Speed is too fast (*2018-09-20 00:00:00*)
    - Note from @jennaj: Noticed mismatched tools across tuto components. The  "Reads mapping" step description states "We have used the HiCExplorer successfully with bwa, bowtie2 and hisat2. In this tutorial we will be using Map with BWA-MEM tool." *However* the "Hands-on: Mapping reads" box has the mapping tool specified as "Map with Bowtie". The tool name doesn't fully match a Galaxy wrapped tool but looks as if it was intended to match "Map with Bowtie for Illumina" tool from some earlier tutorial revision,  but the tool options/settings are actually for "Bowtie2" (tweak SAM/BAM output). The tuto workflow uses "Map with BWA-MEM (Galaxy Version 0.8.0)" which isn't available at EU or ORG (or that version is hidden in the tool panel + tool versions menu).  --------- Punchline ... three different tools are mixed up, at the first step of the tuto after loading the initial fastq inputs. Probably should adjust to make all for either Bowtie2 or BWA-MEM using a version available at EU (so it can be run there). Be nice to have this work at (at least) one of the usegalaxy.* servers :) ORG doesn't include HiC tools. Will ticket this and whatever else is found after reviewing the remainder of steps. (*2019-12-09 00:00:00*)

- **Identification of the binding sites of the Estrogen receptor**


- **Identification of the binding sites of the T-cell acute lymphocytic leukemia protein 1 (TAL1)**

  - Con:
    - A video with step by step instruction. With new versions. (*2019-08-03 00:00:00*)

