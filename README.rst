Showcase of my problem with tox :)
==================================

I would like to test my module with and without cython.  If I do it manually,
it works::

  # test without cython
  $ (rm -f foo.so; python setup.py build_ext --inplace; py.test)

  # test with cython
  $ (export USE_CYTHON=1; rm -f foo.so; python setup.py build_ext --inplace; py.test)

However, if I use tox, it doesn't::

    $ tox
    GLOB sdist-make: /home/antocuni/tmp/toxproblem/setup.py
    py27 inst-nodeps: /home/antocuni/tmp/toxproblem/.tox/dist/toxproblem-0.0.0.zip
    py27 installed: Cython==0.25.1,py==1.4.31,pytest==3.0.3,toxproblem==0.0.0
    py27 runtests: PYTHONHASHSEED='279339209'
    py27 runtests: commands[0] | py.test
    ====================================== test session starts =======================================
    platform linux2 -- Python 2.7.12, pytest-3.0.3, py-1.4.31, pluggy-0.4.0
    rootdir: /home/antocuni, inifile: pytest.ini
    collected 2 items 

    test_foo.py ..

    ==================================== 2 passed in 0.01 seconds ====================================
    cy27 inst-nodeps: /home/antocuni/tmp/toxproblem/.tox/dist/toxproblem-0.0.0.zip
    cy27 installed: Cython==0.25.1,py==1.4.31,pytest==3.0.3,toxproblem==0.0.0
    cy27 runtests: PYTHONHASHSEED='279339209'
    cy27 runtests: commands[0] | py.test
    ====================================== test session starts =======================================
    platform linux2 -- Python 2.7.12, pytest-3.0.3, py-1.4.31, pluggy-0.4.0
    rootdir: /home/antocuni, inifile: pytest.ini
    collected 2 items 

    test_foo.py .F
    ==================================== short test summary info =====================================
    FAIL test_foo.py::test_PYX

    ============================================ FAILURES ============================================
    ____________________________________________ test_PYX ____________________________________________
    test_foo.py:9: in test_PYX
        assert foo.PYX == use_cython
    E   assert False == True
    E    +  where False = foo.PYX
    =============================== 1 failed, 1 passed in 0.04 seconds ===============================
    ERROR: InvocationError: '/home/antocuni/tmp/toxproblem/.tox/cy27/bin/py.test'
    ____________________________________________ summary _____________________________________________
      py27: commands succeeded
    ERROR:   cy27: commands failed
