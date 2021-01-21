from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from rerf.rerfClassifier import rerfClassifier
import xgboost as xgb

def get_names():
    return({"Log. Reg": "#999999", 
         "Lin. SVM":"#f781bf", 
         "SVM":"#a65628", 
         "kNN": "#ffff33", 
         "RF":"#ff7f00", 
         "MLP":"#984ea3",
         "XGB":"#cc99ff",
         "SPORF":"#4daf4a",
         "MORF":"#e41a1c",
         "CNN":"#cab2d6"})

def get_classifiers(
    width,
    height,
    ncores=40,
    n_est = 500,
    projection_matrix="S-RerF",
    clf = None,
    ):

    names = get_names()

    if clf == 'RF':
        classifiers = [
            rerfClassifier(
                n_estimators=n_est,
                projection_matrix="Base",
                max_features="auto",
                n_jobs=ncores,
                random_state=0,
            ),
        ]
        names = {clf: names[clf]}
    else:
        classifiers = [
            LogisticRegression(random_state=0, n_jobs=ncores),
            LinearSVC(),
            SVC(random_state=0),
            KNeighborsClassifier(n_jobs=ncores),
            #RandomForestClassifier(n_estimators=n_est, max_features="auto", n_jobs=ncores),
            rerfClassifier(
                n_estimators=n_est,
                projection_matrix="Base",
                max_features="auto",
                n_jobs=ncores,
                random_state=0,
            ),
            MLPClassifier(random_state=0),
            xgb.XGBClassifier(n_jobs=ncores, random_state=0),
            rerfClassifier(
                n_estimators=n_est,
                projection_matrix="RerF",
                max_features="auto",
                n_jobs=ncores,
                random_state=0,
            ),
            rerfClassifier(
                projection_matrix=projection_matrix,
                max_features="auto",
                n_jobs=ncores,
                n_estimators=n_est,
                oob_score=False,
                random_state=0,
                image_height=height,
                image_width=width,
                patch_height_max=5,
                patch_height_min=1,
                patch_width_max=5,
                patch_width_min=1,
            ),
        ]

    return(names, classifiers)
