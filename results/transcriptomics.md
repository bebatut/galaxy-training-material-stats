- **De novo transcriptome reconstruction with RNA-Seq**
  - Pro:
    - Analysis of the differential gene expression (*20/10/2018*)
    - The explanations and solutions to check our output (*01/12/2018*)
    - The explanation and description is easy to understand. (*20/02/2019*)
  - Con:
    - Visualization with Trackster hands-on section (*20/10/2018*)
    - Explanations of the plots (*01/12/2018*)

- **Differential abundance testing of small RNAs**
  - Pro:
    - the Tutorial is so great and informative (*16/03/2019*)
    - It was wonderful, I am teaching a lab introducing students to bioinformatics, and I am focusing on Galaxy. I wanted to show them how to map RNA-seq reads (small RNAs or mRNAs), I was parsing fasta files for this, but your tutorial already did this. It was immensely helpful. (*09/04/2019*)
  - Con:
    - I wish if you could tell us how to adapt this tutorial to different small RNA species from different organisms, like where can I import the human miRNA, piRNA, .. reference genome from? (*16/03/2019*)
    - For some reason the illumina adapters are not detected.  (*09/04/2019*)
    - Needs another step after "BAM-to-Fastq" is run. Tool outputs "fastq", not "fastqsanger". Redetecting the datatype will work. Other option is to modify the tool to try to assign "fastqsanger" (if the data matches that type, cannot be assume, I'll open an IUC request). See discussion/confusion from a tutorial user here: https://help.galaxyproject.org/t/convert-from-bam-to-fastq/1318 (*20/05/2019*)

- **Downstream Single-cell RNA analysis with RaceID**
  - Pro:
    - Those questions and solutions can help better understanding of the concepts. (*06/08/2019*)

- **GO Enrichment Analysis**
  - Pro:
    - Nicely explained and easy to follow even with own data. (*28/03/2019*)
  - Con:
    - There is no explanation of the graph (colours, %, arrows) and meaning of columns in tabular output (Study#, pvalue, qvalue). Would be nice to shortly describe this with one example GO term. (*28/03/2019*)

- **Network analysis with Heinz**
  - Pro:
    - It was well structured and simply explained (*18/10/2018*)
    - Topic and clarity (DIY is easy) (*18/10/2018*)
    - Easy to follow (*18/10/2018*)
    - Nice clear and good to start a bit further down for speed so it fits the program. (*18/10/2018*)
    - Good introduction by PowerPoint and time enough to finish (*18/10/2018*)
    - step by step manual  (*18/10/2018*)
  - Con:
    - It would be very helpful if the parameter setting on the tools was discussed a bit more and explain the reason why to certain choices (*18/10/2018*)
    - More information about how works the analysis. (*18/10/2018*)
    - note that the use of build list is unclear, perhaps good to move description of how to solve this  up so to prevent questions. (*18/10/2018*)
    - it is good enough (*18/10/2018*)

- **Pre-processing of Single-Cell RNA Data**
  - Pro:
    - It is great (*16/05/2019*)
    - Clear step-by-step instructions (*24/07/2019*)
  - Con:
    - Suggestions of what to do next once the count matrix has been constructed. Can one just use standard methods such as DESeq2 for differential expression? Some examples of PCA? (*24/07/2019*)

- **RNA-Seq reads to counts**
  - Pro:
    - I liked that it takes step by step (*10/01/2019*)

- **RNA-seq counts to genes**
  - Pro:
    - Clear, comprehensive, great screenshots (*18/04/2019*)
    - Easy to follow and showed what our plots/table should look like (*12/08/2019*)
  - Con:
    - Nothing so far (*18/04/2019*)

- **RNA-seq counts to genes and pathways**


- **RNA-seq genes to pathways**
  - Pro:
    - easy to follow. thank you for including a picture of the results for comparison (*19/08/2019*)
  - Con:
    - more analysis/interpretation (*19/08/2019*)

- **Reference-based RNA-Seq data analysis**
  - Pro:
    - İts explanatory feature (*20/09/2018*)
    - The tutorial was very interesting and easy to follow (*27/09/2018*)
    - Topic and completeness of the scope (*19/10/2018*)
    - step-by-step configuration (*03/12/2018*)
    - Nothing :) (*05/01/2019*)
    - How about Computing the Z score of the normalized counts (*02/02/2019*)
    - Good systematic overview. (*08/02/2019*)
    - Nice, easy to follow, thorough (*11/04/2019*)
    - Most complete tuto with lot of aspect. (*12/04/2019*)
    - the "step by step " (*10/05/2019*)
    - Clearly stated. (*30/05/2019*)
    - all (*07/06/2019*)
    - You can work only on the tutorial and if you follow the descriptions carefully, you will get the result you expect to get. (*12/06/2019*)
    - Simplicity (*16/06/2019*)
    - The tutorial is very detailed and helpful. (*10/07/2019*)
    - The easy step by step guide. (*02/08/2019*)
    - Answers provided all along the tutorial to make sure we are correct when performing the tutorial alone (*28/08/2019*)
  - Con:
    - Naming of the output files (*27/09/2018*)
    - I think there is an error: Join two Datasets tool  * with (output of the last Filter tool)  --> Should be with (output of Concatenate tool)  (*19/10/2018*)
    - colors to enhance instructions clarity  (*03/12/2018*)
    - I think it's already good and clear as it is (*05/01/2019*)
    - The website told me that I was over my disk usage limit once I imported the fastqsanger files.  (*08/02/2019*)
    - 1) *The GO results I were slightly different than what the tutorial said, though all the rest of the steps were matching the tutorial's. 2) When uploading the GTF file listed in the tutorial (zenodo link) it was not uploaded as GTF format, I had to manually convert to GTF.  Would definitely be a 5 star review if these were corrected. (*11/04/2019*)
    - Maybe add so MULTIQC (for inferexperiment for example) for an easiest visualisation. (*12/04/2019*)
    - I can not say for sure. (*30/05/2019*)
    - I need to cite this tutorial, how can I cite? If you could send how to do this, I wil be very thankful! lgbragavet@gmail.com is my email, and I'm using Mendeley app to make my references  (*07/06/2019*)
    - waiting time during analyses (*12/06/2019*)
    - Explaining how to get the featureCounts data from another history (drag and drop and say it should be taken from another history in the first place). (*12/06/2019*)
    - Explanation of steps (*16/06/2019*)
    - It's good already! (*02/08/2019*)
    - There might be a bug in one of the tool form values. Search for "transform my data" in the hands on and compare to this short Q&A at Galaxy Help ("Log2(value)" in tuto versus "Log2(value+1) " when the user was given advice. I'll try to find time to test this, too, but anyone who gets there quicker wins the PR :) https://help.galaxyproject.org/t/fatal-error-heatmap2-tool/1288  The heatmap tool has been problematic on and off 6+ years. I'm not even sure if working at usegalaxy.org right now, or if at which, if any, other Galaxy servers. I stopped tracking it after it was broken for so long and just told people to use different tools. I'll review the MTS, etc... maybe some servers need an update.  @jennaj  (*09/08/2019*)
    - Comment section to help people with trouble on this tutorial ? (*28/08/2019*)

- **Reference-based RNAseq data analysis (long)**
  - Pro:
    - interesting and user friendly  (*27/09/2018*)
  - Con:
    - very good  (*27/09/2018*)

- **Visualization of RNA-Seq results with CummeRbund**


- **Visualization of RNA-Seq results with Volcano Plot**
  - Pro:
    - It was very easy to follow (*04/01/2019*)
    - complete, with examples (questions+solutions) (*20/06/2019*)
    - Basic explanations are good and methods and tools used are also understandable. (*11/07/2019*)
    - Crisp and clear explanation  (*02/08/2019*)
    - Easy to understand the hard parts (*08/08/2019*)
  - Con:
    - Tutorial doesn't have any public servers listed. Maybe a tool version conflict? Latest version is 0.0.3 and is installed at EU (and I made a request to add it to ORG). Are probably more tutorials like this -- seems the lists of "instances" is decreasing overall (bigger project, maybe good for the GTN or GCC co-fests) (*09/05/2019*)
    - Providing the code to generate the figures in solutions to help troubleshoot errors can help better. (*11/07/2019*)
    - The representation can be more organized (*02/08/2019*)
    - So far so good (*08/08/2019*)

- **Visualization of RNA-Seq results with heatmap2**


