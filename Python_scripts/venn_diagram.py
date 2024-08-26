import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import seaborn as sns

# Define three sets
sl_mutations = set(["52Y(NP)","105V(NP)","119T(NP)","230L(NP)","450N(NP)","482S(NP)","7S(NS1)","21Q(NS1)","26K(NS1)","53G(NS1)","83S(NS1)","87P(NS1)","116S(NS1)","139N(NS1)","57Q(PA)","86I(PA)","113K(PA)","219L(PA)","277S(PA)","441V(PA)","497K(PA)","548I(PA)","558S(PA)","608S(PA)","59S(PB1)","75E(PB1)","171M(PB1)","172E(PB1)","179M(PB1)","215K(PB1)","264D(PB1)","375S(PB1)","378M(PB1)","399D(PB1)","429R(PB1)","430R(PB1)","515A(PB1)","548F(PB1)","587A(PB1)","694N(PB1)",
"58T(PB2)","109I(PB2)","139V(PB2)","340K(PB2)","362E(PB2)","441D(PB2)","463V(PB2)","464M(PB2)","478I(PB2)","495V(PB2)","591K(PB2)","616V(PB2)","631M(PB2)","649V(PB2)","676T(PB2)","701N(PB2)"
])

ca_mutations =set(["52H(NP)","105M(NP)","119I(NP)","230F(NP)","450N(NP)","482N(NP)","7L(NS1)","21R(NS1)","26E(NS1)","53D(NS1)","83S(NS1)","87P(NS1)","116S(NS1)","139N(NS1)","57R(PA)","86M(PA)","113R(PA)","219I(PA)","277P(PA)","441V(PA)","497R(PA)","548M(PA)","558L(PA)","608S(PA)","59S(PB1)","75D(PB1)","171V(PB1)","172E(PB1)","179I(PB1)","215R(PB1)","264E(PB1)","375S(PB1)","378L(PB1)","399G(PB1)","429K(PB1)","430K(PB1)","515S(PB1)","548L(PB1)","587P(PB1)","694N(PB1)", 
"58A(PB2)","109V(PB2)","139I(PB2)","340R(PB2)","362G(PB2)","441N(PB2)","463I(PB2)","464L(PB2)","478I(PB2)","495I(PB2)","591Q(PB2)","616I(PB2)","631L(PB2)","649I(PB2)","676A(PB2)","701D(PB2)"])

hu_mutations=set(["52Y(NP)","105T(NP)","119V(NP)","230F(NP)","450S(NP)","482S(NP)","7S(NS1)","21R(NS1)","26G(NS1)","53D(NS1)","83S(NS1)","87S(NS1)","116C(NS1)","139N(NS1)","57R(PA)","86M(PA)","113K(PA)","219L(PA)","277H(PA)","441M(PA)","497K(PA)","548M(PA)","558S(PA)","608T(PA)",
"59T(PB1)","75E(PB1)","171M(PB1)","172E(PB1)","179I(PB1)","215R(PB1)","264E(PB1)","375S(PB1)","378L(PB1)","399G(PB1)","429K(PB1)","430K(PB1)","515S(PB1)","548L(PB1)","587V(PB1)","694N(PB1)","58T(PB2)","109V(PB2)","139V(PB2)","340K(PB2)","362E(PB2)","441D(PB2)","463I(PB2)","464L(PB2)","478I(PB2)","495V(PB2)","591R(PB2)","616I(PB2)","631M(PB2)","649V(PB2)","676T(PB2)","701D(PB2)"])


# Calculate intersections and differences
intersection_set1_set2 = sl_mutations & ca_mutations
intersection_set1_set3 = sl_mutations & hu_mutations
intersection_set2_set3 = ca_mutations & hu_mutations
intersection_set1_set2_set3 = sl_mutations & ca_mutations & hu_mutations

only_set1 = sl_mutations - ca_mutations - hu_mutations
only_set2 = ca_mutations - sl_mutations - hu_mutations
only_set3 = hu_mutations - sl_mutations - ca_mutations
set1_set2_only = (sl_mutations - hu_mutations) & (ca_mutations - hu_mutations)
set1_set3_only = (sl_mutations - ca_mutations) & (hu_mutations - ca_mutations)
set2_set3_only = (ca_mutations - sl_mutations) & (hu_mutations - sl_mutations)

# Create the Venn diagram
fig,ax = plt.subplots(figsize = (18,16))
venn_diagram = venn3(subsets=(len(only_set1), len(only_set2), len(set1_set2_only),
                              len(only_set3), len(set1_set3_only), len(set2_set3_only),
                              len(intersection_set1_set2_set3)),
                     set_labels=('', '', ''))

only_set1_text = [""]
only_set2_text = [""]
only_set3_text = [""]


set1_3_intersection = ["52Y(NP)","482S(NP)", "\n","7S(NS1)", "\n","113K(PA)","219L(PA)","497K(PA)","558S(PA)","\n","75E(PB1)", "171M(PB1)","\n","58T(PB2)","139V(PB2)","340K(PB2)","362E(PB2)", "441D(PB2)", "495V(PB2)","631M(PB2)", "649V(PB2)", "676T(PB2)"]

set1_2_intersection = ["450N(NP)", "\n","87P(NS1)", "116S(NS1)", "\n","441V(PA)", "608S(PA)"]

set2_3_intersection = ["230F(NP)","\n", "21R(NS1)","53D(NS1)","\n","57R(PA)", "86M(PA)", "548M(PA)", "\n","179I(PB1)","215R(PB1)", "264E(PB1)", "378L(PB1)","399G(PB1)", "429K(PB1)","430K(PB1)","515S(PB1)","548L(PB1)", "\n","109V(PB2)", "463I(PB2)","464L(PB2)", "616I(PB2)", "701D(PB2)"]


set_1_2_3_intersection = ["83S(NS1)", "139N(NS1)","\n","172E(PB1)","375S(PB1)","694N(PB1)", "\n","478I(PB2)"]



# Set labels for each subset
venn_diagram.get_label_by_id('100').set_text('\n'.join(map(str, only_set1_text)))
venn_diagram.get_label_by_id('010').set_text('\n'.join(map(str, only_set2_text)))
venn_diagram.get_label_by_id('001').set_text('\n'.join(map(str, only_set3_text)))
venn_diagram.get_label_by_id('110').set_text('\n'.join(map(str, set1_2_intersection)))
venn_diagram.get_label_by_id('101').set_text('\n'.join(map(str, set1_3_intersection)))
venn_diagram.get_label_by_id('011').set_text('\n'.join(map(str, set2_3_intersection)))
venn_diagram.get_label_by_id('111').set_text('\n'.join(map(str, set_1_2_3_intersection)))


# Customize colors (since venn3 does not directly support color customization, we modify afterward)
venn_diagram.get_patch_by_id('100').set_color('violet')   # Sea lion only
venn_diagram.get_patch_by_id('010').set_color('blue')    # Cattle only
venn_diagram.get_patch_by_id('001').set_color('pink')     # Human only
#venn_diagram.get_patch_by_id('110').set_color('purple')   # Sea lion and Cattle
#venn_diagram.get_patch_by_id('101').set_color('purple')   # Sea lion and Human
#venn_diagram.get_patch_by_id('011').set_color('cyan')     # Cattle and Human
venn_diagram.get_patch_by_id('111').set_color('gray')     # Sea lion, Cattle, and Human


venn_diagram.get_label_by_id('100').set_fontweight("bold")
venn_diagram.get_label_by_id('010').set_fontweight("bold")
venn_diagram.get_label_by_id('001').set_fontweight("bold")
venn_diagram.get_label_by_id('110').set_fontweight("bold")
venn_diagram.get_label_by_id('101').set_fontweight("bold")
venn_diagram.get_label_by_id('011').set_fontweight("bold")
venn_diagram.get_label_by_id('111').set_fontweight("bold")

venn_diagram.get_label_by_id('100').set_color("black")
venn_diagram.get_label_by_id('010').set_color("black")
venn_diagram.get_label_by_id('001').set_color("black")
venn_diagram.get_label_by_id('110').set_color("black")
venn_diagram.get_label_by_id('101').set_color("black")
venn_diagram.get_label_by_id('011').set_color("black")
venn_diagram.get_label_by_id('111').set_color("black")



venn_diagram.get_label_by_id('101').set_fontsize(12)
venn_diagram.get_label_by_id('011').set_fontsize(12)
venn_diagram.get_label_by_id('111'). set_fontsize(12)


print(sns.color_palette("rocket")[0])



for patch_id in ['100', '010', '001', '110', '101', '011', '111']:
    patch = venn_diagram.get_patch_by_id(patch_id)
    patch.set_edgecolor('black')  # Border color
    patch.set_linewidth(2)

venn_diagram.get_patch_by_id('100').set_alpha(0.25)   # Sea lion only
venn_diagram.get_patch_by_id('010').set_alpha(0.25)   # Cattle only
venn_diagram.get_patch_by_id('001').set_alpha(0.25)   # Human only
venn_diagram.get_patch_by_id('110').set_alpha(0.5)   # Sea lion and Cattle
venn_diagram.get_patch_by_id('101').set_alpha(0.5)   # Sea lion and Human
venn_diagram.get_patch_by_id('011').set_alpha(0.5)   # Cattle and Human
venn_diagram.get_patch_by_id('111').set_alpha(0.5)   # Sea lion, Cattle, and Human

# Save the diagram to a PDF file
plt.savefig("/Users/ranjananataraj/Desktop/venn_sample.pdf")

# Display the diagram
plt.show()
