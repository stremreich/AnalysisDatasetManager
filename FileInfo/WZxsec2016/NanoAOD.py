import socket
uwlogin = "uwlogin" in socket.gethostname() 
uw = "hep.wisc.edu" in socket.gethostname() 
info = {
    "wz3lnu_powheg" : {
        "DAS" : "/WZTo3LNu_13TeV-powheg-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1*/NANOAODSIM",
        "plot_group" : "wz-powheg"
    },
    "wzjj_ewk" : {
        "DAS" : "/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1*/NANOAODSIM",
        "plot_group" : "wzjj_ewk"
    },
    "DYm50__LO" : {
        "DAS" : "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv4-PU2017RECOSIMstep_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6_ext1-v1*/NANOAODSIM",
        "plot_group" : "DYm50__LO"
    },
    "zg" : {
        "DAS" : "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1*/NANOAODSIM",
        "plot_group" : "zg"
    },
    "tt_lep" : {
        "DAS" : "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1*/NANOAODSIM",
        "plot_group" : "tt_lep"
    },
    "ttz" : {
        "DAS" : "/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv4-PU2017_12Apr2018_Nano14Dec2018_102X_mc2017_realistic_v6-v1*/NANOAODSIM",
        "plot_group" : "ttz"
    },
    "zz4l_powheg" : {
        "DAS" : "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1*/NANOAODSIM",
        "plot_group" : "zz4l_powheg"
    },
    "data_SingleMuon_Run2017B-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2017B-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2017C-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2017C-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2017D-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2017D-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2017E-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2017E-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2017F-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2017F-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017B-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2017B-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017C-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2017C-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017D-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2017D-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017E-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2017E-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017F-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2017F-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2016B-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2016B_ver2-Nano1June2019_ver2-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2016C-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2016C-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2016D-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2016D-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2016E-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2016E-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2016F-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2016F-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2016G-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2016G-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2016H-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2016H-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2016B-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2016B_ver2-Nano1June2019_ver2-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2016C-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2016C-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2016D-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2016D-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2016E-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2016E-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2016F-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2016F-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2016G-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2016G-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2016H-Nano1June2019-v1" : {
        "DAS" : "/SingleElectron/Run2016H-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2018A-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2018A-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2018B-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2018B-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2018C-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2018C-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2018D-Nano1June2019-v1" : {
        "DAS" : "/SingleMuon/Run2018D-Nano1June2019-v1*/NANOAOD",
        "plot_group" : "data"
    }
}
