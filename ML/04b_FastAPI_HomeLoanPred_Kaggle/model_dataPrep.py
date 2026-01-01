def data_prep(data):
    # Mapping for Ordinals

    # 1. mapping for all quality related columns
    qualmap = {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'None': 0}

    # List of ord features using 1st mapping
    ocols = ['FireplaceQu', 'GarageQual', 'GarageCond', 'BsmtCond', 'BsmtCond', 'ExterQual', 'ExterCond', 'HeatingQC', 'KitchenQual','PoolQC' ]

    for col in ocols:
        data[col] = data[col].map(qualmap)

    # 2. New map for exposure
    expmap = {'Gd': 4, 'Av': 3, 'Mn': 2, 'No': 1, 'None': 0}
    data['BsmtExposure'] = data['BsmtExposure'].map(expmap)

    # 3. New map for finishing

    finmap = {'GLQ': 6, 'ALQ': 5, 'BLQ': 4, 'Rec': 3, 'LwQ': 2, 'Unf': 1, 'None': 0}
    data['BsmtFinType1'] = data['BsmtFinType1'].map(finmap)
    data['BsmtFinType2'] = data['BsmtFinType2'].map(finmap)


    data['TotalBuiltUp'] = data['TotalBsmtSF']+data['GrLivArea']
    data['TotalBath']=  data['BsmtFullBath']+data['FullBath']+ (0.5 * data['BsmtHalfBath']) + (0.5 * data['HalfBath'])
    data['TotalProchArea'] = data['OpenPorchSF']+data['EnclosedPorch']+ data['3SsnPorch']+data['ScreenPorch']
    data['HouseAge'] = data['YrSold'] - data['YearBuilt']
    data['RemodelAge'] = data['YrSold'] - data['YearRemodAdd']
    data['IsRemodeled'] = (data['YearBuilt'] != data['YearRemodAdd'] ).astype(int)
    data['HasBasement'] = data['TotalBsmtSF'].apply(lambda x: 1 if x>0 else 0)
    data['HasGarage'] = data['GarageArea'].apply(lambda x: 1 if x>0 else 0)
    data['Is NewHouse'] = (data['YearBuilt']==data['YrSold']).astype(int)

    return(data)