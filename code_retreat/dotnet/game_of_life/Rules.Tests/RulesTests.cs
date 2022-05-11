using System;
using Xunit;
using GameOfLife.Rules;

namespace Rules.Tests
{
    public class RulesTestSuite
    {
        [Fact]
        public void TestWrong()
        {
            // arrange
            SubRules rules=new SubRules();
            // act
            int result=rules.Multiply(2,3);
            // assert
            Assert.False(result==9);
            Assert.True(result==6);
        }
    }
}
