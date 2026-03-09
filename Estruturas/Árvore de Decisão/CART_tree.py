import pandas as pd # type: ignore
import numpy as np # type: ignore

# Dataset of the restaurant example 
data = {
    'Exemplo': [f'x{i}' for i in range(1, 13)],
    'Alt.': ['Sim', 'Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Sim', 'Não', 'Sim'],
    'Bar': ['Não', 'Não', 'Sim', 'Não', 'Não', 'Sim', 'Não', 'Não', 'Sim', 'Sim', 'Não', 'Sim'],
    'Sex/Sab': ['Não', 'Não', 'Não', 'Sim', 'Sim', 'Não', 'Não', 'Não', 'Sim', 'Sim', 'Não', 'Sim'],
    'Fome': ['Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Sim'],
    'Clientes': ['Alguns', 'Cheio', 'Alguns', 'Cheio', 'Cheio', 'Alguns', 'Nenhum', 'Alguns', 'Cheio', 'Cheio', 'Nenhum', 'Cheio'],
    'Pr.': ['$$$', '$', '$', '$', '$$$', '$$', '$', '$$', '$', '$$$', '$', '$'],
    'Chuva': ['Não', 'Não', 'Não', 'Sim', 'Não', 'Sim', 'Sim', 'Sim', 'Sim', 'Não', 'Não', 'Não'],
    'Res.': ['Sim', 'Não', 'Não', 'Não', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Não'],
    'Tipo': ['Francês', 'Tailandês', 'Burguer', 'Tailandês', 'Francês', 'Italiano', 'Burguer', 'Tailandês', 'Burguer', 'Italiano', 'Tailandês', 'Burguer'],
    'Estim.': ['0-10', '30-60', '0-10', '10-30', '>60', '0-10', '0-10', '0-10', '>60', '10-30', '0-10', '30-60'],
    'VaiEsperar': ['Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Sim']
}


df = pd.DataFrame(data)

def print_tree(tree, indent=0, branch_label="Root"):
    """
    Recursively prints the decision tree structure.
    
    Args:
        tree: The current node or leaf of the tree.
        indent: The current level of indentation for visual hierarchy.
        branch_label: The label of the branch that led to this node.
    """
    prefix = "    " * indent
    
    # Base Case: If the tree node is a leaf (not a dictionary), print the prediction
    if not isinstance(tree, dict):
        print(f"{prefix}└── {branch_label}: ✅ {tree}")
        return

    # Recursive Step: If it's a node, extract the condition and traverse
    for condition, branches in tree.items():
        print(f"{prefix}└── {branch_label}: [{condition}]")
        
        # Recursively print the 'Sim' and 'Não' branches
        if 'Sim' in branches:
            print_tree(branches['Sim'], indent + 1, "Sim")
        if 'Não' in branches:
            print_tree(branches['Não'], indent + 1, "Não")


def gini_impurity(target_col):
    """
    Calculate the Gini Impurity for a target column.
    Formula: $Gini = 1 - \sum_{i=1}^{n} (p_i)^2$
    where p_i is the probability of an item belonging to class i.
    """
    _, counts = np.unique(target_col, return_counts=True)
    prob = counts / counts.sum()
    return 1 - np.sum(prob**2)

def cart_split(df, target, features):
    """
    Find the best binary split for the dataset using the Gini Index.
    Iterates through all features and possible values to minimize weighted Gini.
    """
    best_gini = float('inf')
    best_split = None
    
    for f in features:
        for value in df[f].unique():
            # Create a binary partition: True (matches value) vs False (does not match)
            subset_left = df[df[f] == value]
            subset_right = df[df[f] != value]
            
            # Skip if the split results in an empty partition
            if subset_left.empty or subset_right.empty:
                continue
                
            # Calculate weighted Gini impurity for the resulting split
            gini_left = gini_impurity(subset_left[target])
            gini_right = gini_impurity(subset_right[target])
            n = len(df)
            
            # Calculate the weighted average of the impurities
            weighted_gini = (len(subset_left)/n) * gini_left + (len(subset_right)/n) * gini_right
            
            # Update the best split if this one is purer (lower Gini)
            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_split = (f, value, subset_left, subset_right)
                
    return best_split

def build_tree_cart(df, target, features):
    """
    Recursively construct the CART decision tree.
    """
    # Base case 1: If all labels are the same, return the label (pure node)
    if len(np.unique(df[target])) == 1:
        return np.unique(df[target])[0]
    
    # Base case 2: If no features are left to split on, return the majority vote
    if not features:
        return df[target].mode()[0]
    
    # Find the best binary split
    split = cart_split(df, target, features)
    
    # If no valid split is found, return the majority label
    if not split:
        return df[target].mode()[0]
    
    feature, value, left_df, right_df = split
    
    # Structure the binary tree with 'Sim' (Left/True) and 'Não' (Right/False) branches
    tree = {f"{feature} == {value}": {
        "Sim": build_tree_cart(left_df, target, features),
        "Não": build_tree_cart(right_df, target, features)
    }}
    return tree

# Define features and build the tree
features = ['Alt.', 'Bar', 'Sex/Sab', 'Fome', 'Clientes', 'Pr.', 'Chuva', 'Res.', 'Tipo', 'Estim.']
decision_tree_cart = build_tree_cart(df, 'VaiEsperar', features)
print_tree(decision_tree_cart)