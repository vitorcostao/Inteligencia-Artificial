import pandas as pd # type: ignore
import numpy as np # type: ignore


def print_tree(tree, indent=0, branch_label=""):
    prefix = "    " * indent
    connector = f"── {branch_label}: " if branch_label else ""

    if not isinstance(tree, dict):
        symbol = "✅" if tree == "Sim" else "❌"
        print(f"{prefix}{connector}{symbol} {tree}")
        return

    feature, branches = next(iter(tree.items()))
    print(f"{prefix}{connector}[{feature}]")

    items = list(branches.items())
    for i, (value, subtree) in enumerate(items):
        print_tree(subtree, indent + 1, branch_label=value)



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

def entropy(target_col):
    """Calculates the Shannon entropy for a given target column."""
    elements, counts = np.unique(target_col, return_counts=True)
    prob = counts / counts.sum()
    return -np.sum(prob * np.log2(prob))

def id3(df, target, features):
    """
    Recursively constructs a decision tree using the ID3 algorithm.
    
    Args:
        df: The training dataset as a pandas DataFrame.
        target: The name of the label column.
        features: A list of feature column names to evaluate.
        
    Returns:
        dict: A nested dictionary representing the decision tree.
    """
    # Base Case: If all samples belong to the same class, return that class
    if len(np.unique(df[target])) <= 1:
        return np.unique(df[target])[0]
    
    # Base Case: If no features remain, return the most frequent label
    if not features:
        return df[target].mode()[0]
    
    general_entropy = entropy(df[target])
    gain = [] 
    
    # Calculate Information Gain for each attribute to determine the best split
    for f in features:
        entropy_f = 0
        for value in df[f].unique():
            sub = df[df[f] == value]
            prob = len(sub) / len(df) 
            entropy_f += prob * entropy(sub[target])
        gain.append(general_entropy - entropy_f)
    
    # Select the attribute with the highest gain
    best_feature = features[np.argmax(gain)]
    tree = {best_feature: {}}
    remaining_features = [f for f in features if f != best_feature]
    
    # Build branches recursively
    for value in df[best_feature].unique():
        sub = df[df[best_feature] == value]
        
        if sub.empty:
            tree[best_feature][value] = df[target].mode()[0]
        else:
            tree[best_feature][value] = id3(sub, target, remaining_features)
    
    return tree
    
features = ['Alt.', 'Bar', 'Sex/Sab', 'Fome', 'Clientes', 'Pr.', 'Chuva', 'Res.', 'Tipo', 'Estim.']
decision_tree = id3(df, 'VaiEsperar', features)
print_tree(decision_tree)