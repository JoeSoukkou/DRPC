# -*- coding: cp1256 -*-
#PYTHON CODE
#Codeé Par Youcef Soukkou , 01/03/2018 15:00
AMINO_ACIDS  = ['ALA','PRO','CYS','HIS','GLY','SER','GLUn','ASPn','VAL','ASP','GLU','LEU','METH','TRYP','ISOL','PHENY','TYR','THR','ARG','LYS']
DNA = ['A','G','T','C']
RNA = ['A','G','U','C']
global SEQUENCE_TYPE;
def conv_RNA2PROTEIN(CODONS, NUM_CODONS):
	cnt = 0
	PROTEIN = list()
	while (cnt <= NUM_CODONS-1):
		if(CODONS[cnt] == 'AUG'):
			PROTEIN.append('METHIONINE')
		elif(CODONS[cnt] == 'UAG' or  CODONS[cnt] == 'UAA' or CODONS[cnt] == 'UGA'):
			PROTEIN.append('STOP')
		elif(CODONS[cnt] == 'UUU' or  CODONS[cnt] == 'UUC'):
			PROTEIN.append('PHENYALANINE')
		elif(CODONS[cnt] == 'UUA' or  CODONS[cnt] == 'UUG' or CODONS[cnt] == 'CUU' or CODONS[cnt] == 'CUC' or CODONS[cnt] == 'CUA' or CODONS[cnt] == 'CUG'):
			PROTEIN.append('LEUCINE')
		elif(CODONS[cnt] == 'AUU' or  CODONS[cnt] == 'AUC' or CODONS[cnt] == 'AUA'):
			PROTEIN.append('ISOLEUCINE')
		elif(CODONS[cnt] == 'GUU' or  CODONS[cnt] == 'GUC' or CODONS[cnt] == 'GUA' or CODONS[cnt] == 'GUG' ):
			PROTEIN.append('VALINE')
		elif(CODONS[cnt] == 'GCU' or  CODONS[cnt] == 'GCC' or CODONS[cnt] == 'GCA' or CODONS[cnt] == 'GCG'):
			PROTEIN.append('ALANINE')
		elif(CODONS[cnt] == 'UCU' or  CODONS[cnt] == 'UCC' or CODONS[cnt] == 'UCA' or CODONS[cnt] == 'UCG'):
			PROTEIN.append('SERINE')
		elif(CODONS[cnt] == 'CCU' or  CODONS[cnt] == 'CCC' or CODONS[cnt] == 'CCA' or CODONS[cnt] == 'CCG'):
			PROTEIN.append('PROLINE')
		elif(CODONS[cnt] == 'ACU' or  CODONS[cnt] == 'ACC' or CODONS[cnt] == 'ACA' or CODONS[cnt] == 'ACG'):
			PROTEIN.append('THRIONINE')
		elif(CODONS[cnt] == 'GCU' or  CODONS[cnt] == 'GCC' or CODONS[cnt] == 'GCA' or CODONS[cnt] == 'GCG'):
			PROTEIN.append('ALANINE')
		elif(CODONS[cnt] == 'UAU' or  CODONS[cnt] == 'UAC'):
			PROTEIN.append('TYROSINE')
		elif(CODONS[cnt] == 'CAU' or  CODONS[cnt] == 'CAC'):
			PROTEIN.append('HISTIDINE')
		elif(CODONS[cnt] == 'CAA' or  CODONS[cnt] == 'CAG'):
			PROTEIN.append('GLUTAMINE')
		elif(CODONS[cnt] == 'AAU' or  CODONS[cnt] == 'AAC'):
			PROTEIN.append('ASPARGININE')
		elif(CODONS[cnt] == 'AAA' or  CODONS[cnt] == 'AAG'):
			PROTEIN.append('LYSINE')
		elif(CODONS[cnt] == 'GAU' or  CODONS[cnt] == 'GAC'):
			PROTEIN.append('ASPARTIC ACID')
		elif(CODONS[cnt] == 'GAG' or  CODONS[cnt] == 'GAA'):
			PROTEIN.append('GLUTAMIC ACID')
		elif(CODONS[cnt] == 'UGG'):
			PROTEIN.append('TRYPTOPHAN')
		elif(CODONS[cnt] == 'UGU' or  CODONS[cnt] == 'UGC'):
			PROTEIN.append('CYSTEINE')
		cnt = cnt + 1 
	print ('Protein chain : ' + str(PROTEIN))		
        start_initiate()

def conv_DNA2RNA(CODONS, NUM_CODONS):
        RNA_FRA = list()
        solu = list()
        list_1D = 0
        list_2D = 0
        while (list_1D <= NUM_CODONS-1):
                list_2D = 0
                solu = []
                while (list_2D <= 2):
                        if (CODONS[list_1D][list_2D] == 'T'):
                                solu.append(CODONS[list_1D].replace('T', 'A'))
                        elif (CODONS[list_1D][list_2D] == 'A'):
                                solu.append(CODONS[list_1D].replace('A', 'U'))
                        elif (CODONS[list_1D][list_2D] == 'G'):
                                solu.append(CODONS[list_1D].replace('G', 'C'))
                        elif (CODONS[list_1D][list_2D] == 'C'):
                                solu.append(CODONS[list_1D].replace('C', 'G'))        
                        list_2D = list_2D + 1
                RNA_FRA.append(solu[0][0]+solu[1][1]+solu[2][2]) 
                list_1D = list_1D + 1        
        print("RNA STRAND  : " + str(RNA_FRA))
	conv_RNA2PROTEIN(RNA_FRA, NUM_CODONS)
                 

def split_DNA_RNA(DNA_RNA_STRAND, TYPE):
    
	counter = 0
	old_NUM = 0
	length = len(DNA_RNA_STRAND)
	NUM_CODONS = length / 3
	CODONS = list()
	while (counter <= length-1):
		counter = counter + 3
		CODONS.append(DNA_RNA_STRAND[old_NUM:counter]) 
		old_NUM = counter
        if (TYPE == 'DNA'):
                conv_DNA2RNA(CODONS, NUM_CODONS)
        elif (TYPE == 'RNA') :
                conv_RNA2PROTEIN(CODONS, NUM_CODONS)

        
        

def reffers(SEQUENCE_TYPE, STRAND):
	if (SEQUENCE_TYPE == "DNA"):
		split_DNA_RNA(STRAND, SEQUENCE_TYPE)
	elif(SEQUENCE_TYPE == "RNA"):
		split_DNA_RNA(STRAND, SEQUENCE_TYPE)

def start_initiate():
        DNA_RNA = raw_input("DNA or RNA ? ")
        if (DNA_RNA) : 
                if(len(DNA_RNA) % 3 == 0):
                        i= 0 
                        while (i<= len(DNA_RNA)) : 
                                if (DNA_RNA[i] == 'U'):
                                        SEQUENCE_TYPE = "RNA"
                                        print (" processing RNA ...")
                                        reffers(SEQUENCE_TYPE, DNA_RNA)
                                        break
                                        

                                elif (DNA_RNA[i] == 'T'): 
                                        SEQUENCE_TYPE = "DNA"
                                        print ("Processing the DNA ... ")
                                        reffers(SEQUENCE_TYPE, DNA_RNA)
                                        break	
                                        
                                        
                                i = i + 1

                

                else : 
                        print ("THE DNA/RNA SEQUENCE ISN'T WELL THOUGH TO BE CONVERTED !!! TRY AGAIN !! ")	
start_initiate()
