#!/bin/bash

node -v

root_path=$PWD;

geppetto_repo="https://github.com/openworm/org.geppetto.frontend.git -b griddle-update";
extension_repo="https://github.com/MetaCell/geppetto-scidash.git -b refactoring";

geppetto_path="./static/org.geppetto.frontend";
geppetto_app_path="$geppetto_path/src/main/webapp";
extension_path="$geppetto_app_path/extensions/geppetto-scidash";
sample_config_path="./service/geppetto/GeppettoConfiguration.json";
actual_config_path="$geppetto_app_path/GeppettoConfiguration.json";

git clone $geppetto_repo $geppetto_path;
git clone $extension_repo $extension_path;

cd $geppetto_app_path;

npm install

cd $root_path;

cp $sample_config_path $actual_config_path;