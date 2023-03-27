# This script translates a citations.csv file exported from Google Scholar
# into markdown format for a publications page. It also fills a YAML file
# with publication information.

import numpy as np
import pandas as pd


# Special formatting categories and membership

name_categories = [
    'group_member',
    'pi',
]

name_properties = dict(
    group_member = ['Barton, J', 'Garcia Noceda, M'],
    pi = ['Barton, J'],
)

paper_name_categories = [
    'equal_contributions',
    'co_corresponding',
]

paper_link_categories = [
    'pdf_link',
    'si_link',
    'repo_link',
    'post_link',
]

paper_properties = {
    'https://doi.org/10.1101/2021.12.31.21268591': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/lee-sc2-transmission.pdf',
        repo_link = 'https://github.com/bartonlab/paper-SARS-CoV-2-inference'
    ),
    'https://doi.org/10.1093/molbev/msac199': dict(
        co_corresponding = ['McKay, M', 'Barton, J'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/sohail-epistasis.pdf',
    ),
    'https://doi.org/10.1128/mSystems.00122-21': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/lordan-supplements.pdf',
    ),
    'https://doi.org/10.1128/msystems.00095-21': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/rando-pathogenesis.pdf',
    ),
    'https://doi.org/10.1073/pnas.2022496118': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/murakowski-vaccine.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/murakowski-vaccine-si.pdf',
    ),
    'https://doi.org/10.1038/s41587-020-0737-3': dict(
        equal_contributions = ['Sohail, M', 'Louie, R'],
        co_corresponding = ['McKay, M', 'Barton, J'],
        repo_link = 'https://github.com/bartonlab/paper-MPL-inference',
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/sohail-mpl.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/sohail-mpl-si.pdf',
    ),
    'https://doi.org/10.1371/journal.pntd.0008676': dict(
        co_corresponding = ['Quadeer, A', 'McKay, M', 'Barton, J'],
        repo_link = 'https://github.com/faraz107/Robust-DENV-Vaccine-Candidates',
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/ahmed-dengue.pdf',
    ),
    'https://doi.org/10.1007/s10955-021-02716-2': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/shivam-spin.pdf',
    ),
    'https://doi.org/10.1371/journal.pgen.1009009': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/zhang-epistasis.pdf',
    ),
    'https://doi.org/10.1093/bioinformatics/btz925': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/quadeer-mpf-bml.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/quadeer-mpf-bml-si.pdf',
        repo_link = 'https://github.com/ahmedaq/MPF-BML-GUI',
    ),
    'https://doi.org/10.1103/PhysRevE.101.012309': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/rizzato-compression.pdf',
    ),
    'https://doi.org/10.1038/s41467-019-14174-2': dict(
        #co_corresponding = ['Chakraborty, A', 'McKay, M'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/quadeer-poliovirus.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/quadeer-poliovirus-si.pdf',
    ),
    'https://doi.org/10.1128/JVI.01920-18': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/vibholm-reservoir-compartments.pdf',
    ),
    'https://doi.org/10.1073/pnas.1813512115': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/lu-reservoir-rebound.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/lu-reservoir-rebound-si.pdf',
    ),
    'https://doi.org/10.1084/jem.20180936': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/cohen-reservoir-rebound.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/cohen-reservoir-rebound-si.pdf',
    ),
    'https://doi.org/10.1093/ve/vez029': dict(
        equal_contributions = ['Barton, J', 'Rajkoomar, E'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-nef.pdf',
        repo_link = 'https://github.com/johnbarton/paper-Nef-modeling'
    ),
    'https://doi.org/10.7554/eLife.33038': dict(
        equal_contributions = ['Ovchinnikov, V', 'Louveau, J', 'Barton, J'],
        #co_corresponding = ['Karplus, M', 'Chakraborty, A'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/ovchinnikov-bnab-flexibility.pdf',
        repo_link = 'https://github.com/johnbarton/paper-bnAb-flexibility'
    ),
    'https://doi.org/10.1073/pnas.1717765115': dict(
        equal_contributions = ['Louie, R', 'Kaczorowski, K'],
        #co_corresponding = ['Chakraborty, A', 'McKay, M'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/louie-env-fitness.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/louie-env-fitness-si.pdf',
    ),
    'https://doi.org/10.7554/eLife.27810.001': dict(
        #co_corresponding = ['Ranganathan, R', 'Kuriyan, J'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/bandaru-ras.pdf',
    ),
    'https://doi.org/10.7554/eLife.27810': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/bandaru-ras.pdf',
    ),
    'https://doi.org/10.1088/1361-6633/aa574a': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/chakraborty-vaccine-design.pdf',
    ),
    'https://doi.org/10.1073/pnas.1617789113': dict(
        equal_contributions = ['Lorenzi, J', 'Cohen, Y'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/lorenzi-qqvoa.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/lorenzi-qqvoa-si.pdf',
    ),
    'https://doi.org/10.1093/bioinformatics/btw328': dict(
        co_corresponding = ['Barton, J', 'Cocco, S'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-ace.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/barton-ace-si.pdf',
        repo_link = 'https://github.com/johnbarton/ACE',
    ),
    'https://doi.org/10.1038/ncomms11660': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-hiv-escape.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/barton-hiv-escape-si.pdf',
    ),
    'https://doi.org/10.1103/PhysRevE.93.022412': dict(
        equal_contributions = ['Butler, T', 'Barton, J'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/butler-protease.pdf',
    ),
    'https://doi.org/10.1007/s10955-015-1441-4': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-pfam-entropy.pdf',
    ),
    'https://doi.org/10.1073/pnas.1415386112': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-hiv-basins.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/barton-hiv-basins-si.pdf',
    ),
    'https://arxiv.org/abs/1412.8065': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-insulator-remarks.pdf',
    ),
    'https://doi.org/10.1103/PhysRevE.90.012132': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-large-pseudocounts.pdf',
    ),
    'https://doi.org/10.1371/journal.pcbi.1003776': dict(
        equal_contributions = ['Mann, J', 'Barton, J', 'Ferguson, A'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/mann-gag-landscape.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/mann-gag-landscape-si.pdf',
    ),
    'https://doi.org/10.1103/PhysRevE.88.062705': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/shekhar-hiv.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/shekhar-hiv-si.pdf',
    ),
    'https://doi.org/10.1016/j.bpj.2013.01.056': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-insulator.pdf',
        si_link = '{{ site.baseurl }}/assets/pdf/papers/barton-insulator-si.pdf',
    ),
    'https://doi.org/10.1088/1742-5468/2013/03/P03002': dict(
        co_corresponding = ['Barton, J', 'Cocco, S'],
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-neural.pdf',
    ),
    'https://doi.org/10.1007/s10955-011-0279-7': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-gabc.pdf',
    ),
    'https://doi.org/10.1088/1751-8113/44/6/065005': dict(
        pdf_link = '{{ site.baseurl }}/assets/pdf/papers/barton-gcabc.pdf',
    )
}


# Style modifications

style_prefix = dict(
    group_member = '<b>',
)

style_suffix = dict(
    group_member = '</b>',
    equal_contributions = '<sup>=</sup>',
    co_corresponding = '<sup>c</sup>',
)

style_link = dict(
    preprint = '[preprint]',
    doi = '[journal link]',
    pdf_link = '[pdf]',
    si_link = '[si]',
    repo_link = '[code]',
    post_link = '[post]',
)

# Main functions

def usage():
    print("")
    
    
def match_name(csv_name, l_f):
    """ Returns true if input name in CSV form loosely matches name in last/first format """
    csv_last = csv_name.split(',')[0]
    csv_init = ''.join([n[0] for n in csv_name.split(',')[1].split()])[0]
    l_f_last = l_f.split(', ')[0]
    l_f_init = l_f.split(', ')[1]
    if csv_last.lower()==l_f_last.lower() and csv_init.lower()==l_f_init.lower(): return True
    else: return False


def main(**kwargs):

    df = pd.read_csv('_data/citations.csv', encoding="latin-1")
    
    # Get information and sort by years
    
    cols = ['Authors', 'Title', 'Publication', 'Volume', 'Number', 'Pages', 'Year', 'Publisher', 'Month', 'Day', 'DOI']
    
    years = np.unique(np.array(df.Year))
    years = years[np.argsort(years)[::-1]]
    
    # Record pubs by year in markdown
    
    f = open('menu/papers.md', 'w')
    f.write("""---\nlayout: page\ntitle: Papers\n---\n\n""")
    f.write("""See [Google Scholar](https://scholar.google.com/citations?user=ItAcAOMAAAAJ) for the most recent and complete list of publications.\n\n""")
    
    f.write('<small>%s equal contributions\n<br></small>' % (style_suffix['equal_contributions']))
    f.write('<small>%s co-corresponding authors\n<br></small>' % (style_suffix['co_corresponding']))
    f.write('\n')
    
    g = open('_data/publications.yml', 'w')
    
    h = open('_data/cv_publications.dat', 'w')
    
    for y in years:
        f.write('<h3>%d</h3>\n' % y)
        
        dfY    = df[df.Year==y]
        months = np.unique(np.array(dfY.Month))
        months = months[np.argsort(months)[::-1]]
        
        for m in months:
            dfYM = dfY[dfY.Month==m]
            dfYM = dfYM.sort_values(['Day'], ascending=[False])
            
            for index, paper in dfYM.iterrows():
                author_list = paper.Authors.split(';')
                doi         = str(paper.DOI)
                
                for i in range(len(author_list)):
                    if author_list[i][0] == ' ':
                        author_list[i] = author_list[i][1:]
            
                # Paper title
                f.write('<small><b>%s</b><br>' % paper.Title)
                g.write("- title: '%s'\n  authors: " % paper.Title)
            
                # Author list
                for a in author_list:
                    if len(a)>0:
                        a_prefix = ''
                        a_suffix = ''
                
                        # Stylize name by category
                        for c in name_categories:
                            for n in name_properties[c]:
                                if match_name(a, n):
                                    if c in style_prefix:
                                        a_prefix += style_prefix[c]
                                    if c in style_suffix:
                                        a_suffix += style_suffix[c]
                
                        # Stylize name by paper
                        if doi in paper_properties:
                            for c in paper_name_categories:
                                if c in paper_properties[doi]:
                                    for n in paper_properties[doi][c]:
                                        if match_name(a, n):
                                            if c in style_prefix:
                                                a_prefix += style_prefix[c]
                                            if c in style_suffix:
                                                a_suffix += style_suffix[c]
                
                        a_init = ''.join([n[0] for n in a.split(',')[1].split()])
                        a_last = a.split(',')[0]
                        f.write('%s%s%s' % (a_prefix, a_last+' '+a_init, a_suffix))
                        g.write('%s%s%s' % (a_prefix, a_last+' '+a_init, a_suffix))
                        h.write('%s%s%s' % (a_prefix, a_last+' '+a_init, a_suffix))
                        if author_list.index(a)<len(author_list)-2:
                            f.write(', ')
                            g.write(', ')
                            h.write(', ')
                        else:
                            f.write('<br>')
                            g.write('\n')
                            h.write('. <i>%s</i>. ' % paper.Title)
            
                # Journal information and links
                f.write('%s' % paper.Publication)
                g.write("  journal: '%s'\n" % paper.Publication)
                h.write('%s' % paper.Publication)
                if 'rxiv' in doi.lower():
                    f.write(' <a href="%s">%s</a>' % (doi, style_link['preprint']))
                    g.write('  preprint: true\n')
                else:
                    f.write(' <a href="%s">%s</a>' % (doi, style_link['doi']))
                    g.write('  doi: %s\n' % doi)
            
                if doi in paper_properties:
                    for c in paper_link_categories:
                        if c in paper_properties[doi]:
                            f.write(' <a href="%s">%s</a>' % (paper_properties[doi][c], style_link[c]))
                f.write('</small>\n\n')

                # Volume/Number/Pages/Year
                if not np.isnan(paper.Volume):
                    g.write('  volume: %d\n' % paper.Volume)
                    h.write(' %d' % paper.Volume)
                else:
                    g.write('  volume: NA\n')
                if not np.isnan(paper.Number):
                    g.write('  number: %d\n' % paper.Number)
                    h.write(' (%d)' % paper.Number)
                else:
                    g.write('  number: NA\n')
                g.write('  pages: %s\n' % paper.Pages)
                g.write('  year: %d\n\n' % paper.Year)
                h.write(': %s (%d). doi:%s\n' % (paper.Pages, paper.Year, doi))
            
    f.close()
    g.close()
    h.close()

if __name__ == '__main__': main()
