LIBRARY_DIR=h4_scripts/lib

help:  # 顯示命令列表
	@cat Makefile | grep -e '^\([[:alpha:]].*\):' | sed -e 's/^\(.*\):.*#\(.*\)/make \1 \t #\2/g'

setup: # 安裝 dependencies
	test -d _logs || mkdir _logs
	test -d 3rd || mkdir 3rd
	test -d 3rd/wikidot/ || ( cd 3rd; git clone git://github.com/gabrys/wikidot.git; cd wikidot/; git apply ../0001-php-syntax-deprecated.patch )
	sudo apt-get install -y tidy

run-wiki:   # wididot 之個人頁面 rebuild
	./h4_wikidot_rebuild 2>&1 | tee _logs/h4_wikidot_rebuild_$$(date "+%Y-%m-%d_%H%M%S").log

run-fb:   # 發送 facebook 活動通知
	# ./h4_create_fb_event.py | tee _logs/h4_create_fb_event.py_$$(date "+%Y-%m-%d_%H%M%S").log
	# ./h4_cli --fb invite    | tee _logs/h4_cli_fb_$$(date "+%Y-%m-%d_%H%M%S").log

log: # 顯示最新產生的 log
	echo $$(find _logs -type f | xargs ls -t | head -1)

logedit: # 編輯最新產生的 log
	$$EDITOR $$(find _logs -type f | xargs ls -t | head -1)

clean: # 清除執行期的暫存檔
	find . -type f -name '*.pyc' -print0 | xargs -0 rm -v

chkpy3: # 檢查 python3 語法
	for ff in `find ./ $(LIBRARY_DIR) -maxdepth 1 -type f -name '*.py' | xargs file | grep 'Python script' | cut -d: -f1`; \
	do \
		echo "====== $$ff ======"; \
		python3 -m py_compile $$ff ;\
	done

chkpy2: # 檢查 python2 語法
	for ff in `find ./ $(LIBRARY_DIR) -maxdepth 1 -type f -name '*.py' | xargs file | grep 'Python script' | cut -d: -f1`; \
	do \
		echo "====== $$ff ======"; \
		python2 -m py_compile $$ff ;\
	done

pep8: # 檢查 PEP-8 語法規範
	for ff in `find ./ $(LIBRARY_DIR) -maxdepth 1 -type f | xargs file | grep 'Python script' | cut -d: -f1`; \
	do \
		pep8 --ignore=E501 $$ff ;\
	done

test: # 函式庫測試
	@env | grep DRY_RUN; \
	if [ $$? -eq 0 ]; then \
		DRY_RUN=$$DRY_RUN nosetests --exe -v test; \
	else \
		DRY_RUN=True nosetests --exe -v test; \
	fi

test_print:  # 函式庫測試及輸出 STDOUT
	@env | grep DRY_RUN; \
	if [ $$? -eq 0 ]; then \
		DRY_RUN=$$DRY_RUN nosetests --nocapture --exe -v test; \
	else \
		DRY_RUN=True nosetests --nocapture --exe -v test; \
	fi

.SILENT: clean

.PHONY: all test clean
