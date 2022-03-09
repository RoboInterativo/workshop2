cd vkapp
npm run build
cd ..
cd web
npm run build
cd ..

rm -rf robo/templates/web
rm -rf robo/templates/vkapp
mkdir robo/templates/web
mkdir robo/templates/vkapp
cp vkapp/build/*  robo/templates/vkapp -r
cp web/build/*  robo/templates/web -r
